"""
Check that changelog conforms to 'Keep A Changelog' style.

See https://keepachangelog.com/en/ for details

EPILOG:
Example:
```
check-changelog --file CHANGELOG.md
```
"""


import logging
import os
import sys

import pydevkit.log.config  # noqa: F401
from pydevkit.argparse import ArgumentParser

from . import __version__
from .changelog import load_changelog
from .git import do_check_tags, do_install_git_hook
from .misc import run_task
from .release import do_release

log = logging.getLogger(__name__)

bool_yes_no = ["yes", "no"]


def get_args():
    p = ArgumentParser(help=__doc__, version=__version__)
    p.add_argument(
        "--check-style",
        help=("check changelog style"),
        choices=bool_yes_no,
        default="yes",
    )
    p.add_argument(
        "--check-tags",
        help=(
            "check that tags are documented. "
            "If value is 'stdin', read tag refs from stdin as pre-push hook "
            "would do. If  'history:N' - check N latest tags, "
            "if 'history' - check all tags"
        ),
        metavar="tags",
    )

    p.add_argument(
        "--install-hook",
        help=("install git 'pre-push' hook"),
        action="store_true",
    )
    p.add_argument(
        "--release",
        help=(
            "add new release section to the changelog. if NAME is 'new', adds "
            "[Unreleased] section. Otherwise, adds NAME release based on "
            "existing [Unreleased] content. Creates CHANGELOG.md if missing"
        ),
        metavar="NAME",
    )
    p.add_argument("-C", help="project dir", dest="topdir", default=".")
    p.add_argument(
        "--file", help="changelog file to check", default="CHANGELOG.md"
    )

    return p.parse_known_args()


def do_checks(args):
    log.info("read %s", args.file)

    cl = run_task("check", "style", load_changelog, {"file": args.file})
    if not cl:
        return False
    if not args.check_tags:
        return True
    return run_task(
        "check",
        "tags '%s'" % args.check_tags,
        do_check_tags,
        cl,
        args.check_tags,
    )


def main():
    args, unknown_args = get_args()
    if unknown_args:
        log.warning("Unknown arguments: %s", unknown_args)
        sys.exit(1)
    if args.topdir != ".":
        try:
            log.info("working dir '%s'", args.topdir)
            os.chdir(args.topdir)
        except Exception as exp:
            log.error("%s", exp)
            sys.exit(1)

    if args.release:
        rc = run_task("release", args.release, do_release, args)
    elif args.install_hook:
        rc = run_task("hook", "install pre-push", do_install_git_hook)
    else:
        rc = run_task("check", args.file, do_checks, args)
    sys.exit(0 if rc else 1)


if __name__ == "__main__":
    main()
