#!/usr/bin/env python

"""map.py"""

import sys
import os

if __name__ == "__main__":

    document_name = os.environ["map_input_file"]
    offset = os.environ["map_input_start"]    
    length = os.environ["map_input_length"]    
    
    line_count = 0
    for line in sys.stdin:
        words = line.strip().split()
        for word in words:
            print('{0},{1},{2}'.format(word,document_name,line_count))
        line_count += 1
