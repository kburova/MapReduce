#!/usr/bin/env python

"""reduce.py"""

import sys

if __name__ == "__main__":
    lines = set()
    for line in sys.stdin:
        lines.add(line.strip())

    lines = sorted(lines)

    for line in lines:
        print(line)
