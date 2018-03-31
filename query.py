import sys
import os

if __name__ == "__main__":
    inverted_index = {}
    with open(sys.argv[1], 'r') as index_file:
        for line in index_file.readlines():
            word,doc,line = line.strip().split(',')
            if word not in inverted_index:
                inverted_index[word] = [(doc,line)]
            else:
                inverted_index[word].append((doc,line))

    while True:
        query = input('Word to search for: ')
        if query in inverted_index:
            for val in inverted_index[query]:
                print(val)
        else:
            print('Word not found!')
