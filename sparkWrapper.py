import os
from pyspark import SparkContext

def splitKeyVal(line):
    terms = line.strip().split(',')
    if terms[0]:
        return (terms[0],(terms[1],terms[2]))

def start(spark):
    inv_index = spark.sparkContext.textFile('output/part-00000')
    inv_index = inv_index.filter(lambda entry: entry.strip().split(',')[1] != '')
    inv_index = inv_index.map(lambda entry: splitKeyVal(entry)).groupByKey()
    inv_index_map = inv_index.collectAsMap()

    line = input('Query the Location of a Word: ')
    while True:
        query = line.strip()
        if query in inv_index_map:
            for loc in inv_index_map[query]:
                print(loc)
        else:
            print('That word was not found!')
        line = input('Query the Location of a Word: ')

if __name__ == "__main__":
    sc = SparkContext("local", "IndexQuery", pyFiles=['sparkWrapper.py', 'output/part-00000'])

    inv_index = sc.textFile('output/part-00000')
    inv_index = inv_index.filter(lambda entry: entry.strip().split(',')[1] != '')
    inv_index = inv_index.map(lambda entry: splitKeyVal(entry)).groupByKey()
    inv_index_map = inv_index.collectAsMap()

    for loc in inv_index_map['tu']:
        print(loc)
