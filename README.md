# MapReduce

## Part 1.Generate stop words.

There are two programs to count words: `mapper.py` and `reducer.py`. 
  - `mapper.py` - read and filter input, handles all the punctuation and capitalization
  - `reducer.py` - counts occurence of each word

Command to run these programs is:

    hadoop jar /usr/local/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
    -files /users/username/mapper.py,/users/username/reducer.py \
    -mapper mapper.py -reducer reducer.py \
    -input /user/username/books/ \
    -output /user/username/output
    
Result of reduction is saved into `/user/username/output/part-00000` file on hdfs.

After we get a list of counts, we send it to `stopwords.py` on stdin and generate a list of stopwords called `list.txt`. It also outputs a threshold for word frequency. We currentely generate 100 stopwords.
    
    kburova@resourcemanager:~$ python stopwords.py < part-00000 
    Threashold:  1308

## Part 2. Building the Inverted Index

## Part 3. Query the Inverted Index
