# 효율적인 Python 코딩법
## tuple
```
test = (1,) + ('Jason', 'M')

print(test)

# (1, 'Jason', 'M')
```

## enumerate
```python
# Collect all possible pairs using combinations()
possible_pairs = [*combinations(pokemon_types, 2)]

# Create an empty list called enumerated_tuples
enumrated_tuples = []

# Add a line to append each enumerated_pair_tuple to the empty list above
for i,pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumrated_tuples.append(enumerated_pair_tuple)

# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumrated_tuples)]
print(enumerated_pairs)
```

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

## Exploratory Data Analysis
### Frequency counts: continent
> df.continent.value_counts(dropna=False)

```python
df.continent.value_counts(dropna=False)

df['continent'].value_counts(dropna=False)
```

### Visualizing single variables with histograms

## Tidying data for analysis
### Tidy data
- Formalize the way we describe the shape of data

# Data Manipulation with pandas
## Transforming data
### Sorting and subsetting

> isin을 활용한 IN 조건절 구현
```python
is_black_or_brown = dogs['color'].isin(['Black','Brown'])
dogs[is_black_or_brown]
```

## Aggregating data
```python

```

## 중복데이터 제거
> 단일 컬럼 기준
```python
unique_dogs = vet_visits.drop_duplicates(subset="name")
```

> 복수 컬럼 기준
```python
unique_dogs = vet_visits.drop_duplicates(subset=["name","breed"])
```
