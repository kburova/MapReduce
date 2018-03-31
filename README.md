# MapReduce

## Part 1.Generate stop words.

There are two programs to count words: `mapper.py` and `reducer.py`. 
  - `map_stop_words.py` - read and filter input, handles all the punctuation and capitalization
  - `reduce_stop_words.py` - counts occurence of each word

Command to run these programs is:

    hadoop jar /usr/local/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
    -files /users/username/map_stop_words.py,/users/username/reduce_stop_words.py \
    -mapper map_stop_words.py -reducer reduce_stop_words.py \
    -input /user/username/books/ \
    -output /user/username/output
    
Result of reduction is saved into `/user/username/output/part-00000` file on hdfs.

After we get a list of counts, we send it to `stopwords.py` on stdin and generate a list of stopwords called `list.txt`. It also outputs a threshold for word frequency. We currentely generate 100 stopwords.
    
    kburova@resourcemanager:~$ python stopwords.py < part-00000 
    Threashold:  1308

## Part 2. Building the Inverted Index

The map and reduce programs for building the inverted index across documents are:
  - `map.py` - read each file, remove stop words, index words by document and line number
  - `reduce.py` - sorts the inverted index entries

Command to run these programs is:

    hadoop jar /usr/local/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
    -files /users/username/map.py,/users/username/reduce.py,/users/username/stop_words.txt \
    -mapper map.py -reducer reduce.py \
    -input /user/username/books/ \
    -output /user/username/output
    
Result of reduction is saved into `/user/username/output/part-00000` file on hdfs. This is expected to overwrite the stop words list.

## Part 3. Query the Inverted Index

The inverted index can then be queried with: `python query.py /user/username/output/part-00000`
The query program will then prompt the user for a word to look up in the inverted index and print the results to stdout.

## Part 4. Spark Integration

The program to integrate the query system on Spark RDDs is in `sparkWrapper.py`. The program can be run by executing the `/bin/pyspark` executable and then importing `sparkWrapper` as a module. Thequery system can then be started by issuing `sparkWrapper.start(spark)`.
