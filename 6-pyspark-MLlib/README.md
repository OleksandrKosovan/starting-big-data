# PySpark. MLlib

### I. MLlib

![alt txt](https://cdn-images-1.medium.com/max/1400/1*b7VXivcK-wBqQJDWjzBszg.png)

MLlib is Apache Spark's scalable machine learning library. [More..](https://spark.apache.org/mllib/)

### II. About Jupyter Notebooks

This tutorial is based on Titanic data from Kaggle website. it has 2 parts:

- First one is using mllib package with rdds, and the mmlib random forest classification. [Here](https://github.com/OleksandrKosovan/starting-big-data/blob/master/6-pyspark-MLlib/1%20-%20Titanic%20using%20mllib%20module.ipynb) :link:

- Second one is using sql dataframes and ml packages, and the ml random forest classification (same principle as in llib). Once it is solved without pipeline, once with pipeline. [Here](https://github.com/OleksandrKosovan/starting-big-data/blob/master/6-pyspark-MLlib/2%20-%20Titanic%20using%20sql%20dataframe%20and%20ml%20module.ipynb) :link:

ml and sql dataframe simplify a lot the preprocessing stages, whereas with mmlib and rdds you often have to create your own functions to process the data.

ml also have a vast range of metrics compared to mllib.

[Source](https://creativedata.atlassian.net/wiki/spaces/SAP/pages/83237142/Pyspark+-+Tutorial+based+on+Titanic+Dataset)
