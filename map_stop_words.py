#!/usr/bin/env python
"""Mapper - parses all the words in input and turns to lower case"""

import sys
import re

# remove 'ed, 's, 'st, 'll and etc.
def remove_apostr(word):
    index = word.find("'")
    if index != -1:
        return word[0:index]
    return word

def remove_punct(word):
    tmp = re.sub('["$@&+>=_<?!:;{}(),.*#[\]-]','', word)
    return tmp

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.replace("--"," ")
        words = line.strip().split()
        for word in words:
            word = remove_apostr(remove_punct(word))
            if word != "":
                print '%s\t%s' % (remove_apostr(word.lower()), 1)
