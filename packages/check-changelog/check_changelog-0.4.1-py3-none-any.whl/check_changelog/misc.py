"""Misc code."""

import logging
import subprocess as sp

import toml

log = logging.getLogger(__name__)


def task_status(ttype, tname, status):
    clrs = {
        "norm": "\033[0m",
        "ok": "\033[32;1m",
        "fail": "\033[31;1m",
        "starting": "\033[32;1m",
    }
    msg = ""
    rc = {
        "clr-off": clrs["norm"],
        "clr-on": clrs[status],
        "type": ttype,
        "name": tname,
        "status": status,
    }
    fmt = "%(clr-on)s%(type)s%(clr-off)s %(name)s: %(clr-on)s%(status)s%(clr-off)s"
    msg += fmt % rc
    return msg


def run_task(ttype, tname, func, *args):
    _norm = "\033[0m"
    _ok = "\033[32;1m"
    _fail = "\033[31;1m"
    log.info("%s", task_status(ttype, tname, "starting"))
    try:
        rc = func(*args)
    except Exception as exc:
        rc = False
        log.error("%s", exc)
        raise
    if rc:
        log.info("%s", task_status(ttype, tname, "ok"))
    else:
        log.error("%s", task_status(ttype, tname, "fail"))
    return rc


def get_host():
    log.debug("get_host")
    host = get_host_pyproject()
    log.debug("get_host_pyproject %s", host)
    if host:
        return host

    host = get_host_git_remote()
    log.debug("get_host_git_remote %s", host)
    if host:
        return host

    return "https://github.com/user/project"


def get_host_pyproject():
    try:
        data = toml.load("pyproject.toml")
        data = data["project"]["urls"]
    except Exception:
        return None
    key = "Repository"
    if key in data:
        url = data[key]
        if url.endswith(".git"):
            url = url[:-4]
        log.debug("project url: from %s key: %s", key, url)
        return url
    key = "Homepage"
    if key in data:
        url = data[key]
        log.debug("project url: from %s key: %s", key, url)
        return url
    return None


def get_host_git_remote():
    txt = sp.check_output("git remote -v", shell=True).strip()
    txt = txt.splitlines()
    if len(txt) == 0:
        return None
    txt = txt[0].decode("utf-8")
    txt = txt.split()[1]  # format is: origin url (type)
    if txt.endswith(".git"):
        txt = txt[:-4]
    return txt
