#### List of code errate

##### Handling Missing data
Chapter 1 : 
df[column] = np.round(imputer.fit_transform(df[[column]]),1) ## Put np.round for consistency accross the whole data
np.round rounds off to the decimal value specified



###### Data Quality metrics and validation
Original
if pd.api.types.is_numeric_dtype(df[column]):
elif pd.api.types.is_string_dtype(df[column])
Corrected 
if pd.api.types.is_numeric_dtype(column):
elif pd.api.types.is_string_dtype(column):


Passing as a column of the pandas dataframe results in keyerror. Instead pass it as Pandas Series 