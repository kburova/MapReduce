#!/usr/bin/env python
"""Mapper - parses all the words in input and turns to lower case"""

import sys

for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        print '%s\t%s' % (word.lower(), 1)
