"""Fail when a shipped JavaScript bundle contains core-js older than 3.3.5.

Older core-js runs feature checks that write `constructor` on a real RegExp and
Promise. In V8 (Chrome, Edge) that write turns off the RegExp and Promise fast
paths for the whole page. After that, String#split, #match, #replace and
#search with a RegExp are up to 80 times slower, also in other libraries on
the page. core-js 3.3.4 and 3.3.5 fixed this (zloirock/core-js#306, #679).

Usage: python .github/check_corejs.py FILE...
"""

import re
import sys
from pathlib import Path

MINIMUM = (3, 3, 5)
# core-js registers itself in a shared store: {version:"3.1.3",mode:"global",...}
MARKER = re.compile(rb"""version\s*:\s*["'](\d+)\.(\d+)\.(\d+)["']\s*,\s*mode\s*:""")


def main(paths):
    if not paths:
        print("error: no bundles given")
        return 1
    failed = False
    for path in paths:
        file = Path(path)
        if not file.is_file():
            print(f"error: {path}: file not found")
            failed = True
            continue
        found = {
            tuple(int(part) for part in m.groups()) for m in MARKER.finditer(file.read_bytes())
        }
        names = ", ".join(".".join(map(str, version)) for version in sorted(found)) or "none"
        old = [version for version in found if version < MINIMUM]
        if old:
            failed = True
            print(f"error: {path}: core-js {names}, older than 3.3.5")
        else:
            print(f"ok: {path}: core-js {names}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
