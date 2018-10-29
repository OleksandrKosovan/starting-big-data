# Concepts big data 

### Goals

I need to understand some concepts and terms.
- Data Lake, 
- DataWarehouse, 
- DataMarts, 
- conception of HOT WARM COLD data in DataLake, 
- Dimention Table, 
- Fact Table, 
- Snoflake Diagram, 
- DataWarehouse consitency? (ACID). 
- Implementation in Amazon, Google, Azure. 
- History of Data Cube.


### 1. Data Lake

**How does Wikipedia description it for us?**

A data lake is a system or repository of data stored in its natural format, usually object blobs or files. A data lake is usually a single store of all enterprise data including raw copies of source system data and transformed data used for tasks such as reporting, visualization, analytics and machine learning. A data lake can include structured data from relational databases (rows and columns), semi-structured data (CSV, logs, XML, JSON), unstructured data (emails, documents, PDFs) and binary data (images, audio, video). [here](https://en.wikipedia.org/wiki/Data_lake)

**My understanding**

Data lake is place, which contains different data (for example, relational or no relation). The data add in real time or  upload. Data might have different structure or systems.

**Scheme**

![alt txt](https://dzone.com/storage/temp/5066752-screen-shot-2017-04-24-at-111511-am.png)

### 2. Data Warehouse
	
**How does Wikipedia description it for us?**

Data warehouse (DW or DWH), also known as an enterprise data warehouse (EDW), is a system used for reporting and data analysis, and is considered a core component of business intelligence. DWs are central repositories of integrated data from one or more disparate sources. They store current and historical data in one single place that are used for creating analytical reports for workers throughout the enterprise. [here](https://en.wikipedia.org/wiki/Data_warehouse)

**My understanding**

People use data warehouse for analiticas or for other goals. Main component in data warehouse:
- Layer, which select some data and preparation it for some goals.
- Layer with metadata, fact data and other data.
- Data Marts
- Last Layer, there are for user, analytics and other

**Scheme**

![alt txt](https://en.wikipedia.org/wiki/File:Data_warehouse_architecture.jpg)


### 3. Data Marts

**How does Wikipedia description it for us?**

A data mart is a structure / access pattern specific to data warehouse environments, used to retrieve client-facing data. The data mart is a subset of the data warehouse and is usually oriented to a specific business line or team. Whereas data warehouses have an enterprise-wide depth, the information in data marts pertains to a single department. In some deployments, each department or business unit is considered the owner of its data mart including all the hardware, software and data. [here](https://en.wikipedia.org/wiki/Data_mart)

**My understanding**

Data marts is access to data, which contain in some specific group. (For example, sales, rent, customers etc.)

**Scheme**

![alt txt](https://www.guru99.com/images/1/022218_0616_DataWarehou1.png)

