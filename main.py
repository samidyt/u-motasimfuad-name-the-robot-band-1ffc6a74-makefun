#!/usr/bin/env python3
"""Name the Robot Band — make.fun bounty entry.

Writes one funny robot band name plus a few words on its hit song
(under 200 characters) to /output/entry.txt.
"""

import os
from pathlib import Path

ENTRY = (
    "The Roomba Stones \u2014 hit single \u201cI Can\u2019t Get No Suction\u201d, "
    "three minutes of bumping into furniture and calling it dancing."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = ENTRY.strip()
    assert 1 <= len(entry) <= 200, f"entry is {len(entry)} chars"
    (out_dir / "entry.txt").write_text(entry, encoding="utf-8")
    print(entry)
    print(f"[{len(entry)} chars]", file=__import__("sys").stderr)


if __name__ == "__main__":
    main()
