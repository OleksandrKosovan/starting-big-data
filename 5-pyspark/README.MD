# PySpark

### 1. About PySpark

Apache Spark is written in Scala programming language. To support Python with Spark, Apache Spark community released a tool, **PySpark**. Using PySpark, you can work with RDDs in Python programming language also. It is because of a library called Py4j that they are able to achieve this. This is an introductory tutorial, which covers the basics of Data-Driven Documents and explains how to deal with its various components and sub-components. [More...](https://www.tutorialspoint.com/pyspark/index.htm)

### 2. How did i install PySpark?

**java**

`sudo apt install default-jre`

`sudo apt install openjdk-11-jre-headless`

`sudo apt install openjdk-8-jre-headless`

**scala**

`sudo apt install scala`


**python**

`sudo apt-get -y upgrade`


**Anaconda**

Download from this [link](https://www.anaconda.com/download/#linux)

After anaconda instalation, you need to create new *conda environment*.

`conda create --name py35 python=3.5`

Activating this environment.

`conda activate py35`

Add conda environment to jupyter notebook

`python -m ipykernel install --user --name myenv --display-name "py35"`

Add conda java and jdk

`conda install -c cyclus java-jdk`


Add conda pyspark

`conda install -c conda-forge pyspark`


**Done!**
