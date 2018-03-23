#!/usr/bin/env python
"""reduce.py"""

import sys

target_key = None
count = 0

for line in sys.stdin:
    doc,key,value = line.strip().split(',')

    if target_key == key:
        count += int(value)
    else:
        if target_key:
            print('{0},{1},{2}'.format(doc,target_key,count))
        target_key = key
        count = int(value)

if target_key == key:
    print('{0},{1},{2}'.format(doc,target_key,count))
