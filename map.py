#!/usr/bin/env python

"""map.py"""

import sys
import os
import re

def remove_apostr(word):
	index = word.find("'")
	if index != -1:
		return word[0:index]
	return word

def remove_punct(word):
	tmp = re.sub('["$@&+>=_<?!:;{}(),.*#[\]-]','', word)
	return tmp

if __name__ == "__main__":
    document_name = os.environ["map_input_file"]
    offset = os.environ["map_input_start"]    
    length = os.environ["map_input_length"]    

    if '/' in document_name:
        document_name = document_name.split('/')[-1]

    stop_words = []
    with open('stop_words.txt','r') as sw:
        for line in sw.readlines():
            stop_words.append(line.strip())

    line_count = 1
    for line in sys.stdin:
        words = line.strip().split()
        for word in words:
            word = remove_apostr(remove_punct(word))
            if (word != "") and (word not in stop_words):
                print('{0},{1},{2}'.format(word,document_name,line_count))
        line_count += 1
