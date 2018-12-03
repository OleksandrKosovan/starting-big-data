
### HDFS (*Hadoop Distributed File System*)

![alt txt](http://getindata.com/wp-content/uploads/2014/09/hadoop-hdfs-post-1.jpg)

I used this hadoop tutorial - [link here](https://www.tutorialspoint.com/hadoop/index.htm)

1. Setting Up Hadoop

`export HADOOP_HOME=/usr/local/hadoop`

2. Before proceeding further, you need to make sure that Hadoop is working fine.

`$HADOOP_HOME/bin/hadoop version`

3. Starting HDFS

`$HADOOP_HOME/bin/hadoop namenode -format`

`/usr/local/hadoop/sbin/start-dfs.sh`

4. Inserting Data into HDFS - [link](https://www.tutorialspoint.com/hadoop/hadoop_hdfs_operations.htm) :link:


**bin/hadoop fs -** fs commands [link](https://hadoop.apache.org/docs/r2.4.1/hadoop-project-dist/hadoop-common/FileSystemShell.html) :link:
