#!/usr/bin/env python3
"""Meme Sprint entry: copy the finished meme image to the output directory.

The meme itself (entry.png, 1024x1024, under 1 MiB) is rendered before the
run and shipped in this repository. This program only validates it and
copies it byte for byte to /output/entry.png, using the standard library
alone so nothing about the grading machine (fonts, Pillow) can break it.

It never deletes or replaces the output directory: it only creates it
when it does not exist yet.
"""

import hashlib
import os
import struct
import sys

MAX_BYTES = 1048576
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print("error: " + message, file=sys.stderr)
    return 1


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    target = os.path.join(out_dir, "entry.png")

    if not os.path.isfile(source):
        return fail("entry.png is missing next to main.py")

    with open(source, "rb") as handle:
        data = handle.read()

    if len(data) > MAX_BYTES:
        return fail("entry.png is %d bytes, over the 1048576 limit" % len(data))
    if not data.startswith(PNG_MAGIC):
        return fail("entry.png is not a PNG file")
    if len(data) < 33 or data[12:16] != b"IHDR":
        return fail("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_SIDE or height > MAX_SIDE:
        return fail("entry.png is %dx%d, over the 1024x1024 limit" % (width, height))

    os.makedirs(out_dir, exist_ok=True)
    with open(target, "wb") as handle:
        handle.write(data)

    written = os.path.getsize(target)
    if written != len(data):
        return fail("wrote %d bytes, expected %d" % (written, len(data)))
    # Verify the copy before reporting success: re-read the output and
    # compare it byte for byte with the shipped image, so a truncated or
    # corrupted write can never pass silently.
    with open(target, "rb") as handle:
        copied = handle.read()
    if copied != data:
        return fail("output differs from entry.png after writing")
    digest = hashlib.sha256(data).hexdigest()[:16]
    print("wrote %s (%dx%d, %d bytes, sha256 %s...)"
          % (target, width, height, written, digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
