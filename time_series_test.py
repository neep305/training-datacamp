import pandas as pd

df = pd.read_csv('./dataset/austin_airport_departure_data_2015_july.csv', parse_dates=True)

print(df.head())