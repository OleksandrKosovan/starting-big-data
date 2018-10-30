# Data cube

### 1. Definition

**Data cube** is a multi-dimensional ("n-D") array of values. Typically, the term datacube is applied in contexts where these arrays are massively larger than the hosting computer's main memory; examples include multi-Terabyte/Petabyte data warehouses and time series of image data. [here](https://en.wikipedia.org/wiki/Data_cube)

![alt txt](https://pythonhosted.org/cubes/_images/cube-dims_and_cell.png)

### 2. Data cube and Python

I finded many interesting links for implementation data cube with python.
- [cubes.databrewery.org](http://cubes.databrewery.org/index.html)  :link:
- [Cubes - OLAP Framework](https://pythonhosted.org/cubes/)  :link:

First, i created 3D-array with numpy. [Jupyter Notebook](https://github.com/OleksandrKosovan/starting-big-data/blob/master/3-data-cube/1-data-cube-simple-sample.ipynb)  :link:


### 3. PostgreSQL and Data Cube

**1.** I used this [tutorial](http://www.postgresqltutorial.com/postgresql-cube/). **Note**: *in this tutorial, you will learn how to use the PostgreSQL CUBE to generate multiple grouping sets.*

**2.** I finded data, which contained information about sales (*date, location and products*). [Link](https://github.com/OleksandrKosovan/starting-big-data/blob/master/3-data-cube/data-cube-postgreSQL/data/Sample-Superstore.csv).  :link: And i selected only data, that i need.

**3.** Next step, i import this data with PostgreSQL. [Link](https://github.com/OleksandrKosovan/starting-big-data/blob/master/3-data-cube/data-cube-postgreSQL/create-data-cube/import-csv) :link:

**4.** Finish, i created data cube with this data. [Link](https://github.com/OleksandrKosovan/starting-big-data/blob/master/3-data-cube/data-cube-postgreSQL/create-data-cube/data-cube-sql)  :link:

**Details**

The query generates all possible grouping sets based on the dimension columns specified in `CUBE`. The CUBE subclause is a short way to define multiple grouping sets so the following are equivalent:

`
SELECT 
/n	orderdate, 
	city, 
	product 
FROM 
	sales
GROUP BY
	CUBE(orderdate,city,product);
`

AND

`
/*
SELECT 
	orderdate, 
	city, 
	product 
FROM 
	sales
GROUPING SETS(
	(orderdate,city,product),
	(orderdate,city),
	(orderdate,product),
	(city,product),
	(orderdate),
	(city),
	(product),
	()
)
*/
`
