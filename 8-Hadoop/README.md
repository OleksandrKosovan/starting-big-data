# Hadoop

![alt txt](https://www.edvancer.in/wp-content/uploads/2016/02/Hadoop_elephants400px.jpg)

### 1. How to Install Hadoop in Stand-Alone Mode on Ubuntu 18.04

I think, the best source with installing information is digital ocean. [Link](https://www.digitalocean.com/community/tutorials/how-to-install-hadoop-in-stand-alone-mode-on-ubuntu-18-04) :link:

### 2. Get started

**Now we should be able to run Hadoop:**

`$ /usr/local/hadoop/bin/hadoop`

or

`$ PATH=$PATH:/usr/local/hadoop/bin/`

`$ hadoop`

or

`export HADOOP_HOME=/usr/local/hadoop`

`$HADOOP_HOME/bin/hadoop`

**First operation:**

Create a directory called *input* in our home directory and copy Hadoop's configuration files into it to use those files as our data.

`$ mkdir ~/hadoop-folder/input`

`$ cp /usr/local/hadoop/etc/hadoop/*.xml ~/hadoop-folder/input`

Next, we can use the following command to run the MapReduce hadoop-mapreduce-examples program, a Java archive with several options. We'll invoke its grep program, one of the many examples included in hadoop-mapreduce-examples, followed by the input directory, input and the output directory grep_example. The MapReduce grep program will count the matches of a literal word or regular expression. Finally, we'll supply the regular expression allowed[.]* to find occurrences of the word allowed within or at the end of a declarative sentence. The expression is case-sensitive, so we wouldn't find the word if it were capitalized at the beginning of a sentence:

`/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.0.3.jar grep ~/hadoop-folder/input ~/hadoop-folder/grep_example 'allowed[.]*'`

