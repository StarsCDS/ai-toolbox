

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

