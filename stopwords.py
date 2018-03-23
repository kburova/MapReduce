#!/usr/bin/env python

import sys
import operator

words_limit=100
stopwords = {}
for line in sys.stdin:
	word, count = line.strip().split('\t', 1)
	stopwords[word] = int(count)

sw_sorted = sorted(stopwords.items(), key=operator.itemgetter(1), reverse=True)

file = open("list.txt", "w")
for i in range(words_limit):
	file.write(sw_sorted[i][0])
	file.write('\n')
file.close()

print 'Threashold: ', sw_sorted[words_limit][1]
