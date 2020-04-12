import pandas as pd


df = pd.read_csv('./dataset/auto-mpg.csv', index_col="name")

print(df.loc['ford torino'])
