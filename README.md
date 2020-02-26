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