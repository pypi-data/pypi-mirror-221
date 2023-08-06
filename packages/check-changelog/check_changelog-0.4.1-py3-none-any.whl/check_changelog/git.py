"""
Check that git tags are documented in CHANGELOG.md.

See https://keepachangelog.com/en/ for details
"""

import logging
import os
import subprocess as sp
import sys

log = logging.getLogger(__name__)


def do_install_git_hook():
    path = ".git/hooks/pre-push"
    if os.path.exists(path):
        log.warning("remove current '%s'", path)
        os.unlink(path)
    sh = (
        "#!/bin/bash\n\n"
        + sys.argv[0]
        + " --check-tags=stdin --log-level=warning\n"
    )
    open(path, "w").write(sh)
    os.chmod(path, 0o755)
    return True


def get_tags_stdin():
    refs = sys.stdin.readlines()
    log.debug("refs %s", refs)
    pfx = "refs/tags/"
    pfx_len = len(pfx)
    return [r[pfx_len:].split()[0] for r in refs if r.startswith(pfx)]


def get_tags_git(latest=1000):
    cmd = "git tag --list --merged | tac"
    if latest >= 0:
        cmd += " | head -n %d" % latest
    tags = sp.check_output(cmd, shell=True)
    tags = tags.decode(encoding="utf-8", errors="ignore")
    return tags.split()


def get_tags(atags):
    log.debug("tag source: %s", atags)
    tags = None
    if atags == "stdin":
        tags = get_tags_stdin()
    elif atags == "history":
        tags = get_tags_git(-1)
    elif atags.startswith("history:"):
        latest = atags.split(":")[1]
        try:
            latest = int(latest)
        except Exception:
            log.error("can't get latest from '%s'", latest)
            latest = -1
        tags = get_tags_git(latest)
    return tags


def do_check_tags(cl, atags):
    tags = get_tags(atags)
    if not tags:
        return True
    log.info("scan %d tags from '%s' source", len(tags), atags)
    rc = True
    for tag in tags:
        rel = cl.release_find(tag)
        log.debug("rel %s", rel)
        if rel:
            log.info("tag '%s' found at pos %s", tag, rel[0])
        else:
            log.error("tag '%s' not found", tag)
            rc = False
    return rc
