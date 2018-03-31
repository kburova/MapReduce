#!/usr/bin/env python
"""Reducer - read sorted input from mapper, and add up counts for each word"""

from operator import itemgetter
import sys

if __name__ == "__main__":
    curr_count = 0
    curr_word = None

    for line in sys.stdin:
        word, count = line.strip().split('\t', 1)
        count = int(count)
    
        if curr_word != word:
            if curr_word:
                print '%s\t%s' % (curr_word, curr_count)
        
            curr_count = count
            curr_word = word
        else:
            curr_count += count

    if curr_word == word:
        print '%s\t%s' % (curr_word, curr_count)
