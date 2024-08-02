#### List of code errate
Chapter 1 : 
 #### DataOps pipeline for ML model training
 synthetic data added to the provided code 

 #### CI/CD pipeline with Git and DVC
 ##### Install necessary packages
!pip install gitpython dvc

 Please do not change the code provided. It already includes all necessary steps for initializing the repository, tracking dataset and model changes with DVC, running tests, and deploying the model.

 #### Agile DataOps sprints and role interactions
 Placeholder function implementations


#### Handling Missing data
 df[column] = np.round(imputer.fit_transform(df[[column]]),1) ## Put np.round for consistency accross the whole data np.round rounds off to the decimal value specified

#### Data Quality metrics and validation
Original if pd.api.types.is_numeric_dtype(df[column]): elif pd.api.types.is_string_dtype(df[column]) Corrected if pd.api.types.is_numeric_dtype(column): elif pd.api.types.is_string_dtype(column):

Passing as a column of the pandas dataframe results in keyerror. Instead pass it as Pandas Series