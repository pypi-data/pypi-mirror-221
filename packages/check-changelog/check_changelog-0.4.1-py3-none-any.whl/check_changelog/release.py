"""
Add release to CHANGELOG.md.

See https://keepachangelog.com/en/ for details
"""

import logging

from .changelog import load_changelog
from .misc import run_task

log = logging.getLogger(__name__)


def do_release(args):
    kwargs = {
        "missing": "create",
        "template": "tags",
        "file": args.file,
    }
    cl = run_task("check", "style", load_changelog, kwargs)
    if not cl:
        return False
    if not args.release:
        return False
    rc = cl.release_ensure(args.release)
    log.debug("changelog final:\n%s", str(cl))
    cl.save()
    return rc
