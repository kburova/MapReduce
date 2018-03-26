#!/usr/bin/env python

"""reduce.py"""

import sys

if __name__ == "__main__":
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    lines = sorted(lines)

    for line in lines:
        print(line)
