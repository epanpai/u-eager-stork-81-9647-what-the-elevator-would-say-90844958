#!/usr/bin/env python3
"""What the Elevator Would Say — make.fun entry (program/v1).

Writes one line, at most 120 characters, to /output/entry.txt:
the funniest thing an elevator would say if it could talk,
in the elevator's own voice.

Design: the elevator is the building's silent witness. It hears
everything riders say inside it — secrets, arguments, off-key
singing — and answers with a deadpan threat that lands on the
last two words. Elevator-specific (it is the box you ride in),
fresh (no "going down?" / ups-and-downs pun), no setup to explain.
At 106 chars it is also compact: on an exact win-rate tie the
smaller text places first, so every word here earns its place.
"""

import os
import sys

ENTRY = "I've heard your secrets, your arguments, your off-key singing. I know everything about you. I say nothing."


def main() -> int:
    # Gate self-check (mirrors the sealed scorer): UTF-8 text,
    # 1 to 120 characters, not only whitespace, single line.
    if not (1 <= len(ENTRY) <= 120):
        print(f"gate FAIL: entry is {len(ENTRY)} chars, must be 1-120", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("gate FAIL: entry is whitespace only", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("gate FAIL: entry must be a single line", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("gate FAIL: leading/trailing whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Read back and verify byte-for-byte.
    with open(path, "rb") as f:
        back = f.read()
    if back != data:
        print("verify FAIL: written bytes differ from ENTRY", file=sys.stderr)
        return 1

    print(f"wrote {path}: {len(data)} bytes / {len(ENTRY)} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
