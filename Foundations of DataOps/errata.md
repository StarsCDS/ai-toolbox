

# Foundation of DataOps


# 1.1 Introduction to Dataops
## The DataOps Lifecycle

####  DataOps pipeline for ML model training


- Synthetic data has been added to the provided code in the textbook . This generates synthetic customer data for a churn prediction scenario. It creates a dataset with 1000 samples, including customer tenure, two random features, and a binary churn indicator.


#### CI/CD pipeline with Git and DVC

- In the textbook, a basic CI/CD workflow using Git and DVC has been implemented, showcasing how code, data, and model versions can be managed and deployed in a DataOps context. The implementation sets up a Git repository, initializes DVC, creates placeholder dataset and model files, and tracks them with Git and DVC. It then performs simple steps for running tests and deploying. 

#### Agile DataOps sprints

- Each function is a placeholder for a specific task and hence created , added along with the code mentioned in the textbook.  

#### Role interactions in a DataOps project
- Each function is a placeholder for a specific task and hence created , added along with the code mentioned in the textbook.





## Automation collaboration and monitoring 


####  Automated data pipeline with error handling

-  prefect has updated its API new version is **flow** using this ensure run on google colab with the older version i got error the difference is prefect 1.x (old) now changed into prefect 2.x (new)

   **Error handling:**
- changed into centralized error handling using  **execute_task** its ensure the DRY and it works fine



#### Basic monitoring in a data pipeline
- Prefect has updated its API, and the newer version uses flow instead of Flow

  **Result Handling:**
- The use of LocalResult for result handling is not necessary for basic tasks. Prefect handles results efficiently by default, 
    

  **Transformation Logic:**


- The proposed code includes additional transformations (numeric_squared and float_rounded), providing a transformation process. It also removes the unnecessary Local Result and defines the some_transformation function for clarity.
    
    
   **Data Quality Monitoring:**

 - The proposed code includes additional quality checks for the new columns (numeric_squared and float_rounded), ensuring comprehensive data quality monitoring.

   **Flow Definition and Execution:**

 - Using the @flow decorator provides a clearer and more concise way to define the flow. It also aligns with the modern Prefect API, 



# 1.2 Data Types and Processing in DataOps

## Data collection and ingestion strategies


####  Batch data ingestion process using python 

- Synthetic data has been added to the provided code in the textbook


- Used SQLite data base since no need for database credentials or network setup.We can also use PostgreSQL



#### Real-time data streaming using Python and Kafka

- It is assumed the local host for Kafka engine is setup by the user

## Datapreprocessing and quality assurance


####  Handling Missing data

- df[column] = np.round(imputer.fit_transform(df[[column]]),1) 
Put np.round for consistency accross the whole data np.round rounds off to the decimal value specified

#### Data Quality metrics and validation

- Original if pd.api.types.is_numeric_dtype(df[column]): elif pd.api.types.is_string_dtype(df[column]) Corrected if pd.api.types.is_numeric_dtype(column): elif pd.api.types.is_string_dtype(column):

- Passing as a column of the pandas dataframe results in keyerror. Instead pass it as Pandas Series

- Passing as a column of the pandas dataframe results in keyerror. Instead pass it as Pandas Series

# 3.DataOps Infrastructure and Tools

## 3.1 Data Lake vs. Data Warehouse

### Data Lake
* The example demonstrates how raw data can be stored in their original JSON format within a data lake, preserving its flexibility for future analysis and processing.
* This code mounts Google Drive, saves raw JSON data to a file in Google Drive, and then reads and displays the contents of the JSON file. The textbook involves a cloud storage solution like Amazon S3 . 

### Data warehouse architectures
* This code creates an SQLite database with three tables (dim_product, dim_customer, fact_sales), inserts sample data into them, and executes a SQL query to aggregate and summarize sales data by product category and customer segment, displaying the results in a Pandas DataFrame.

### Hybrid approaches: Data lakehouse
* demonstrates how a data lake house can support SQL-like queries on large datasets stored in open formats, combining the flexibility of a data lake with the analytical capabilities of a data warehouse.

## Designing Scalable Data Architectures

### Distributed storage systems
* created a PyArrow table, writes it to a local Parquet file, reads the file back, and converts it to a pandas DataFrame for display. in the code it also lists files in the local directory. This is a basic example of file handling .In contrast to the textbook, using HDFS for such tasks in a Python environment is a more complex approach.

## Tools for Data Storage and Retrieval

### Cloud storage solutions
* The code is mounted to  Google Drive instead of using Amazon S3 for storing and retrieving data as mentioned in the textbook , and saves a pandas DataFrame as a CSV file to Google Drive, and then reads it back into a DataFrame. This contrasts with the textbook's use of Amazon S3 for data storage and retrieval.

### Distributed file systems
* The code mounts Google Drive, writes a pandas DataFrame to a Parquet file on Google Drive, and then reads it back into a DataFrame. The textbook uses HDFS for similar operations, which involves a more complex setup for big data storage and retrieval.

### Database management systems for DataOps

- Used SQLite data base instead of Postgres since no need for database credentials or network setup.


## 3.2 Data integration patterns and best practices 

### Data synchronization methods

- Used SQLite data base instead of Postgres since no need for database credentials or network setup. 
### Implementing incremental loading using Python and pandas:
- **Using SQLite Instead of PostgreSQL**: Changed the database engine to SQLite to make the code runnable in Google Colab, as setting up PostgreSQL in Colab is impractical

### Implementing Error Handling and Recovery in a Data Integration Process Using Python

- **Clear Output Messages:** Added print statements to provide clear feedback on the success of each step in the data integration process




## ETL and ELT processes

### Traditional ETL workflows

- Synthetic data has been added to the provided code in the textbook
- Used SQLite data base instead of Postgres since no need for database credentials or network setup.

### ELT and the modern data stack

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
