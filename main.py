#!/usr/bin/env python3
"""One-line office joke entry.

Writes a single original one-line joke about office life to the path
named by the OUTPUT_PATH environment variable (default /output/entry.txt).
"""
import os

JOKE = (
    "I asked for a raise and got a pizza party instead, so now I'm the "
    "only employee whose salary is measured in slices."
)


def main():
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
