import pandas as pd

sales = pd.read_pickle('./dataset/walmart_sales.pkl')

store_types = sales.drop_duplicates(subset=["store", "type"])
print(store_types.head())


store_depts = sales.drop_duplicates(subset=["store", "department"])
print(store_depts.head())
