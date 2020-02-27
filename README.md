# Streamlined Data Ingestion with pandas

## Importing data from flat files

### Handling errors and missing data

## Modifying imports: parsing dates

# Introduction to Importing Data in Python
## Introduction and flat files

## Importing data from other file types

## Working with relational database in Python
```python
# import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Order.sqlite')

# Perform query: rs
rs = con.execute("SELECT * FROM Order")

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())
```

# Cleaning Data in Python

## Exploring your data
### Diagnose data for cleaning
```python
# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
```python
df = pd.read_csv('dob_job_application_filings_subset.csv')

# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

# Print the head and tail of df_subset
print(df_subset.head())
print(df_subset.tail())


```

##
