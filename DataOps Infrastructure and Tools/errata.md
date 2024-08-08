# 3.DataOps Infrastructure and Tools

## 3.1 Data storage and housing


#### Data Lake
* The example demonstrates how raw data can be stored in their original JSON format within a data lake, preserving its flexibility for future analysis and processing.
* This code mounts Google Drive, saves raw JSON data to a file in Google Drive, and then reads and displays the contents of the JSON file. The textbook involves a cloud storage solution like Amazon S3 . 

#### Data warehouse architectures
* This code creates an SQLite database with three tables (dim_product, dim_customer, fact_sales), inserts sample data into them, and executes a SQL query to aggregate and summarize sales data by product category and customer segment, displaying the results in a Pandas DataFrame.

#### Hybrid approaches: Data lakehouse
* demonstrates how a data lake house can support SQL-like queries on large datasets stored in open formats, combining the flexibility of a data lake with the analytical capabilities of a data warehouse.

## Designing Scalable Data Architectures

#### Distributed storage systems
* created a PyArrow table, writes it to a local Parquet file, reads the file back, and converts it to a pandas DataFrame for display. in the code it also lists files in the local directory. This is a basic example of file handling .In contrast to the textbook, using HDFS for such tasks in a Python environment is a more complex approach.

## Tools for Data Storage and Retrieval

#### Cloud storage solutions
* The code is mounted to  Google Drive instead of using Amazon S3 for storing and retrieving data as mentioned in the textbook , and saves a pandas DataFrame as a CSV file to Google Drive, and then reads it back into a DataFrame. This contrasts with the textbook's use of Amazon S3 for data storage and retrieval.

#### Distributed file systems
* The code mounts Google Drive, writes a pandas DataFrame to a Parquet file on Google Drive, and then reads it back into a DataFrame. The textbook uses HDFS for similar operations, which involves a more complex setup for big data storage and retrieval.

#### Database management systems for DataOps

- Used SQLite data base instead of Postgres since no need for database credentials or network setup.


## 3.2 Data Integration and ETL 

#### Data synchronization methods

- Used SQLite data base instead of Postgres since no need for database credentials or network setup. 

####  Incremental data loading

- **Using SQLite Instead of PostgreSQL**: Changed the database engine to SQLite to make the code runnable in Google Colab, as setting up PostgreSQL in Colab is impractical

#### Error handling and recovery in data integration

- **Clear Output Messages:** Added print statements to provide clear feedback on the success of each step in the data integration process


## ETL and ELT processes

#### Traditional ETL workflows

- Synthetic data has been added to the provided code in the textbook
- Used SQLite data base instead of Postgres since no need for database credentials or network setup.

#### ELT and the modern data stack

- Uses Google Drive as cloud data warehouse instead of Bigquery


## ELT tools and framework 

####  Open-source ETL tools:
- **Airflow setup:** (`/content/airflow/dags`), which is crucial for file handling in environments like Google Colab.

#### Cloud-based ETL service :
 - These are specific to AWS Glue and won't work in Colab. You'll need to use Apache Spark with PySpark directly in Colab for similar tasks.
- so in this code we could use pyspark and mounted with googledrive instead of using aws s3 bucket it save into your google drive

#### Building custom ETL pipelines:
- CSV file for execution, and if no file was uploaded, it resulted in an error when attempting to load data
-  A sample CSV file is created programmatically if no file is uploaded, ensuring that the ETL pipeline has data to work with.




