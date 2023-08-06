"""
Parse changelog and ensure it conforms to the required structure.

See https://keepachangelog.com/en/ for details
"""

import logging
import re
import subprocess as sp
import textwrap
from datetime import datetime
from zoneinfo import ZoneInfo

from markdown_it import MarkdownIt

from .misc import get_host

log = logging.getLogger(__name__)
logging.getLogger("markdown_it").setLevel(logging.INFO)
logging.getLogger(__name__ + ".token").setLevel(logging.INFO)
logging.getLogger(__name__ + ".run").setLevel(logging.INFO)


class Tokens(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.idx = 0
        self.lineno = 0
        self.content = ""
        self.log = logging.getLogger(__name__ + ".token")

    def get(self):
        if self.is_empty():
            return None
        t = self[self.idx]
        if self.log.getEffectiveLevel() == logging.DEBUG:
            self.prn_token(t)
        if t.map:
            self.lineno = t.map[0]
            self.content = t.content
        return self[self.idx]

    def next(self):  # noqa: A003
        if self.is_empty():
            return None
        self.idx += 1
        return self.get()

    def is_empty(self):
        return self.idx >= len(self)

    def consume_until(self, func):
        self.log.debug("consume_until")
        while True:
            t = self.get()
            if not t:
                return
            self.next()
            if func(t):
                return

    def prn_token(self, t, lvl=0):
        attrs = ["type", "tag", "map", "content"]
        rc = {}
        for a in attrs:
            rc[a] = getattr(t, a, None)
        self.log.debug("token[%d]: %s%s", self.idx, " " * lvl, rc)
        if not t.children:
            return
        lvl += 2
        for c in t.children:
            self.prn_token(c, lvl)


class CLError(Exception):
    def __init__(self, msg, token=None, msg_extra="", **kwargs):
        self.token = token
        self.lineno = kwargs.get("lineno")
        self.content = kwargs.get("content")
        self.msg = msg
        self.msg_extra = msg_extra
        rlog = logging.getLogger(__name__ + ".run")
        rlog.debug("%s: %d: %s", self.__class__.__name__, self.lineno, self.msg)

    def __str__(self):
        return self.msg


class CLSyntaxError(CLError):
    pass


class CLNotFoundError(CLError):
    pass


class CLPartiallyFoundError(CLError):
    pass


class Changelog:
    """
    Changelog validation and modification.

    init options
     - url: project url. If values is missing, it will be determined from
       pyproject.toml or git rmotes
     - file: changelog file
     - text: changelog text
     - missing: what to do if changelog is missing or mepty.
        - create: create changelog
        - error: raise an error
     - template: template to create new changelog
        - base: add Unreleased only
        - tags: add git tags and Unreleased
    """

    header = """\
    # Changelog

    ## [Unreleased]

    [Unreleased]: %(url)s
    """

    footer = """\
    ------

    The format is based on [Keep a Changelog][kacl] and [Common Changelog][ccl]
    styles and this project adheres to [Semantic Versioning][semver]

    [semver]: https://semver.org/spec/v2.0.0.html "Semantic Versioning"
    [kacl]: https://keepachangelog.com/en/ "Keep a Changelog"
    [ccl]: https://common-changelog.org/ "Common Changelog"
    """
    defaults = {  # noqa: RUF012
        "missing": "error",
        "template": "tags",
    }

    def __init__(self, **kwargs):
        self.kwargs = {}
        self.kwargs.update(self.defaults)
        self.kwargs.update(kwargs)
        if self.kwargs.get("url") is None:
            self.kwargs["url"] = get_host()
        if self.kwargs.get("upath") is None:
            self.kwargs["upath"] = "releases/tag"

        self._loaded = False
        self._dirty = False
        self.rlog = logging.getLogger(__name__ + ".run")

    def load(self, **kwargs):
        log.debug("load: %s", kwargs)
        # FIXME: reset all vars

        srcs = ["text", "file"]
        func = None
        for key in srcs:
            if key in kwargs:

                def _func(_key=key):
                    _lfunc = getattr(self, "load_" + _key)
                    _lfunc(kwargs)

                func = _func
                break
        if func:
            try:
                func()
            except FileNotFoundError:
                pass
            except Exception as exc:
                log.error("exc: %s", exc)
                raise
        if self._loaded:
            return

        missing = self.get_arg(kwargs, "missing")
        if missing == "create":
            self.create(kwargs)

        if self._loaded:
            return
        msg = "can't load; kwargs %s" % kwargs
        raise Exception(msg)

    def load_file(self, kwargs):
        path = self.get_arg(kwargs, "file")
        text = open(path, "r").read()
        self.load_real(text)
        self._dirty = False

    def load_text(self, kwargs):
        text = self.get_arg(kwargs, "text")
        self.load_real(text)

    def load_real(self, text):
        self._loaded = False
        if isinstance(text, str) and text.isspace():
            msg = "empty changelog"
            raise Exception(msg)

        log.debug("loaded text: %d bytes", len(text))
        self.text = text
        self.state = []
        self.tokens = None
        self.parsed = None
        self.parse()
        self._loaded = True

    def get_arg(self, kwargs, key):
        log.debug("arg: key '%s', kwargs %s", key, kwargs)
        val = kwargs.get(key)
        if isinstance(val, bool) and val is True:
            val = self.kwargs.get(key)
        if not val:
            val = self.kwargs.get(key)
        if not val:
            msg = "no '%s' value set" % key
            raise Exception(msg)
        log.debug("arg: key '%s', value '%s'", key, val)
        return val

    def create(self, kwargs):
        log.debug("create: kwargs %s", kwargs)
        tpl = self.get_arg(kwargs, "template")
        func = getattr(self, "create_" + tpl, None)
        if not func:
            msg = "unknown template '%s'" % tpl
            log.error("%s", msg)
            raise Exception(msg)
        func(kwargs)

    def create_base(self, kwargs):
        log.debug("create_base: kwargs %s", kwargs)
        rc = {
            "title": "Changelog",
            "releases": [],
            "footer": {"text": textwrap.dedent(self.footer)},
        }
        self.text = ""
        self.parsed = rc
        self.release_add(0, name="Unreleased")
        self._loaded = True
        self._dirty = True

    def create_tags(self, kwargs):
        self.create_base(kwargs)
        log.debug("create_tags: kwargs %s", kwargs)
        fmt = "%(refname:strip=2) %(taggerdate:short)"
        cmd = "git tag --format='" + fmt + "' -l --merged | tac"
        tags = sp.check_output(cmd, shell=True)
        tags = tags.decode(encoding="utf-8", errors="ignore")
        tags = tags.splitlines()
        self.parsed["releases"]
        for tag in tags:
            log.debug("found tag %s", tag)
            tmp = tag.split()
            if len(tmp) == 2:  # noqa: PLR2004
                el = {"name": tmp[0], "date": tmp[1]}
                self.release_add(-1, **el)

    def release_del(self, name):
        rel = self.release_find(name)
        if rel is None:
            return
        rels = self.parsed["releases"]
        del rels[rel[0]]
        names = self.parsed["rel_names"]
        del names[name]

    def release_find(self, name):
        key = "releases"
        if key not in self.parsed:
            self.parsed[key] = []
        key = "rel_names"
        if key not in self.parsed:
            self.parsed[key] = {}
        names = self.parsed["rel_names"]
        pos = names.get(name)
        if not pos:
            return None
        for pos, rel in enumerate(self.parsed["releases"]):
            if rel["name"] == name:
                return (pos, rel)
        return None

    def release_add(self, pos, **kwargs):
        date = kwargs.get("date", "")
        if date:
            date = " - " + date
        log.debug("release: %s%s", kwargs["name"], date)
        name = kwargs.get("name")
        rel = self.release_find(name)
        rels = self.parsed["releases"]
        if rel is not None:
            log.error("release '%s' already exists at pos %d", name, rel[0])
            return False

        if kwargs.get("name") != "Unreleased":
            if not kwargs.get("date"):
                dt = datetime.now(tz=ZoneInfo("UTC")).strftime("%Y-%m-%d")
                kwargs["date"] = dt
        if pos < 0:
            rels.append(kwargs)
        else:
            rels.insert(pos, kwargs)
        self.parsed["rel_names"][name] = True
        self._dirty = True
        return True

    def release_ensure(self, name):
        log.debug("release_ensure: %s", name)
        if name == "new":
            name = "Unreleased"
        rel = self.release_find(name)
        log.debug("rel %s", rel)
        if rel:
            log.info("section '%s' already exists", name)
            return True

        if name == "Unreleased":
            return self.release_add(0, name="Unreleased")

        unrel = self.release_find("Unreleased")
        if not unrel:
            log.error("need [Unreleased] section to create release")
            return False

        self.release_del("Unreleased")
        return self.release_add(0, name=name, changes=unrel[1].get("changes"))

    # {{{ string
    def get_rel_url(self, name):
        url = self.kwargs.get("url")
        if name != "Unreleased":
            upath = self.kwargs.get("upath")
            url += "/%s/%s" % (upath, name)
        return url

    def __str__(self):
        rc = []
        if not self.parsed:
            msg = "run parse() first"
            raise Exception(msg)
        pcl = self.parsed
        lines = self.text.splitlines()

        def maps2lines(maps):
            block = []
            for m in maps:
                lim = m[1] if m[1] > 0 else len(lines)
                tmp = list(lines[m[0] : lim])
                while tmp and not tmp[-1].strip():
                    tmp.pop()
                block += ["\n".join(tmp)]
            return block

        def add_text_block(block, name=None):
            if name is None:
                name = ""
            if not isinstance(block, dict):
                return []
            val = block.get("text")
            if isinstance(val, str):
                return [val]
            val = block.get("maps")
            if isinstance(val, list):
                return maps2lines(val)
            val = block.get("map")
            if isinstance(val, list):
                return maps2lines([val])
            return []

        def prn_release(rel):
            rc = []
            name = "Unreleased" if rel["name"] == "Unreleased" else rel["name"]
            tmp = "## [%s]" % name
            val = rel.get("date")
            if val:
                tmp += " - " + val
            rc.append(tmp)
            rc += add_text_block(rel.get("notes"), name="notes")
            changes = rel.get("changes")
            if changes is None:
                changes = []
            for change in changes:
                rc += ["### " + change["type"].title()]
                rc += ["\n".join(add_text_block(change, name="change"))]
            return rc

        def prn_links():
            lrc = []
            for rel in pcl["releases"]:
                url = rel.get("link")
                name = "Unreleased" if rel["name"] == "Unreleased" else rel["name"]
                if url is None:
                    url = self.get_rel_url(name)
                lrc += ["[%s]: %s" % (name, url)]
            return ["\n".join(lrc)]

        val = pcl.get("title")
        rc.append("# " + val)

        rc += add_text_block(pcl.get("notes"), name="notes")
        for v in pcl["releases"]:
            rc += prn_release(v)
        rc += prn_links()

        rc += add_text_block(pcl.get("footer"), name="footer")
        return "\n\n".join(rc) + "\n"

    # }}} noqa: ERA001

    def run(self, func, narg):
        data_len = len(self.state)
        self.state.append({})
        try:
            self.run_real(func, narg)
            rc = self.state[data_len]
            self.rlog.debug("func %s, narg %s: exit %s", func, narg, rc)
            return rc
        except Exception:
            raise
        finally:
            self.rlog.debug("func %s, narg %s: cleanup", func, narg)
            del self.state[data_len:]

    def run_real(self, func, narg):
        count = 0
        while True:
            try:
                self.rlog.debug("func %s, narg %s: enter", func, narg)
                func()
            except CLSyntaxError:
                raise
            except CLNotFoundError as exp:
                if narg == "?" or narg == "*":
                    return
                if narg == "+" and count > 0:
                    return
                if count == 0:
                    raise
                raise CLPartiallyFoundError(exp.msg, exp.token) from exp
            count += 1
            if narg == "?":
                return
            if isinstance(narg, int) and count == narg:
                return
            if (narg == "+" or narg == "*") and count > len(self.tokens):
                return

    def save(self, **kwargs):
        if not self._dirty:
            return
        path = self.get_arg(kwargs, "file")
        log.info("save %s", path)
        open(path, "w").write(str(self))
        self._dirty = False

    # {{{ parsing

    tag2type = {  # noqa: RUF012
        "h1": "heading",
        "h2": "heading",
        "h3": "heading",
        "ul": "bullet_list",
        "li": "list_item",
        "p": "paragraph",
    }

    def get_tokens_info(self):
        return {"lineno": self.tokens.lineno, "content": self.tokens.content}

    def upd_map(self, obj, tmap):
        if not tmap:
            return
        maps = obj.get("maps", [])
        maps.append(tmap)
        obj["maps"] = maps

    def parse(self):
        if self.parsed:
            return self.parsed
        md = MarkdownIt("commonmark", {"breaks": True, "html": True})
        self.tokens = Tokens(md.parse(self.text))

        self.parsed = {"releases": [], "rel_names": {}}
        rc = self.run(self.do_title, narg=1)
        self.parsed.update(rc)
        rc = self.run(self.do_notes, narg="*")
        self.parsed["notes"] = rc
        if rc:
            log.info("notes")
        rc = self.run(self.do_release, narg="+")
        for rel in rc["rels"]:
            self.release_add(-1, **rel)
        rc = self.run(self.do_footer, "?")
        self.parsed["footer"] = rc
        log.debug("self.state: %s", self.state)
        if self.tokens.is_empty():
            return self.parsed
        msg = "out of context"
        raise CLSyntaxError(msg, self.tokens.get(), **self.get_tokens_info())

    def do_item(self, tag, msg, validate):
        t = self.tokens.get()
        if not (t and t.type == self.tag2type[tag] + "_open" and t.tag == tag):
            raise CLNotFoundError(msg, t, **self.get_tokens_info())
        if validate:
            validate(msg)
        self.tokens.consume_until(
            lambda x: x.tag == tag
            and x.type == self.tag2type[tag] + "_close"
            and x.level == t.level
        )

    def do_title(self):
        msg = "expected 'Changelog'"

        def _validate(msg):
            t = self.tokens.next()
            log.info("title: %s", t.content)
            if t.content != "Changelog":
                m1 = "bad title"
                raise CLSyntaxError(m1, t, msg, **self.get_tokens_info())
            self.state[-1]["title"] = t.content

        self.do_item("h1", msg, _validate)

    def do_notes(self):
        def _validate(msg):  # noqa: ARG001
            obj = self.state[-1]
            t = self.tokens.get()
            self.upd_map(obj, t.map)

        self.do_item("p", "", _validate)

    def do_footer(self):
        msg = "expecting footer"
        t = self.tokens.get()
        tag = "hr"
        if not (t and t.type == tag and t.tag == tag):
            raise CLNotFoundError(msg, t, **self.get_tokens_info())
        log.info("footer")
        tmap = list(t.map)
        tmap[1] = -1
        self.state[-1]["map"] = tmap
        self.tokens.consume_until(lambda x: False)  # noqa: ARG005

    # }}} noqa: ERA001

    # {{{ changes

    change_type_names = [  # noqa: RUF012
        "Added",
        "Changed",
        "Deprecated",
        "Removed",
        "Fixed",
        "Security",
    ]
    change_type_len = max([len(k) for k in change_type_names])

    def do_change_block(self):
        rc = self.run(self.do_change_type, narg=1)
        try:
            rc.update(self.run(self.do_change_list, narg="+"))
        except CLNotFoundError as exp:
            raise CLSyntaxError(
                exp.msg, exp.token, **self.get_tokens_info()
            ) from exp
        log.info("  %-7s %s", rc["type"], rc["num"])
        ar = self.state[-1].get("blocks", [])
        ar.append(rc)
        self.state[-1]["blocks"] = ar

    def do_change_type(self):
        msg = "expecting '### <Change Type>'"

        def _validate(msg):
            t = self.tokens.next()
            msg += "; got '%s'" % t.content
            if t.content not in self.change_type_names:
                m1 = "bad change type"
                raise CLSyntaxError(
                    m1,
                    t,
                    "expected one of %s" % self.change_type_names,
                    **self.get_tokens_info()
                )
            self.state[-1]["type"] = t.content.lower()

        self.do_item("h3", msg, _validate)

    def do_change_list(self):
        msg = "expecting unordered list"

        def _validate(msg):  # noqa: ARG001
            obj = self.state[-1]
            t = self.tokens.get()
            self.upd_map(obj, t.map)
            self.tokens.next()
            rc = self.run(self.do_change, narg="+")
            self.state[-1].update(rc)

        self.do_item("ul", msg, _validate)

    def do_change(self):
        msg = "expecting list item"
        self.do_item("li", msg, None)
        count = self.state[-1].get("num", 0)
        self.state[-1]["num"] = count + 1

    # }}} noqa: ERA001

    # {{{ release
    def do_release(self):
        rel = {}
        rc = self.run(self.do_release_header, narg=1)
        rel.update(rc)

        rc = self.run(self.do_notes, narg="*")
        rel["notes"] = rc
        if rc:
            log.info("  notes")

        rc = self.run(self.do_change_block, narg="*")
        if rc:
            rc = rc["blocks"]
            rel["changes"] = rc
        log.debug("release: %s", rel)
        arr = self.state[-1].get("rels", [])
        arr.append(rel)
        self.state[-1]["rels"] = arr

    def do_release_header(self):
        msg = "expected '[Unreleased]' or '[ver] - YYYY-MM-DD'"
        msgr = "expected '[ver] - YYYY-MM-DD'"

        def _validate(msg):
            t = self.tokens.next()
            kids_num_unreleased = 3
            kids_num_released = 4
            if not (
                len(t.children) >= kids_num_unreleased
                and t.children[0].type == "link_open"
                and t.children[0].attrs.get("href")
            ):
                m1 = "no link for release"
                raise CLSyntaxError(m1, t, **self.get_tokens_info())
            self.state[-1]["link"] = t.children[0].attrs.get("href")
            rname = t.children[1].content
            if rname is None:
                m1 = "bad release title"
                raise CLSyntaxError(m1, t, msg, **self.get_tokens_info())
            self.state[-1]["name"] = rname
            if rname == "Unreleased":
                if len(t.children) != kids_num_unreleased:
                    m1 = "bad release title"
                    raise CLSyntaxError(m1, t, msg, **self.get_tokens_info())
                log.info("release: Unreleased")
                return
            if len(t.children) != kids_num_released:
                m1 = "bad release title"
                raise CLSyntaxError(m1, t, msg, **self.get_tokens_info())
            rdate = t.children[3].content
            if not re.search("^ - \\d\\d\\d\\d-\\d\\d-\\d\\d$", rdate):
                m1 = "bad release date"
                raise CLSyntaxError(m1, t, msgr, **self.get_tokens_info())
            self.state[-1]["date"] = rdate.split()[-1]
            log.info(
                "release: %s - %s", self.state[-1]["name"], self.state[-1]["date"]
            )

        self.do_item("h2", msg, _validate)

    # }}} noqa: ERA001


def load_changelog(kwargs):
    cl = Changelog(**kwargs)
    cl.load(**kwargs)
    return cl
