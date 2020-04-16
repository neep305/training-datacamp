import pandas as pd
import numpy as np

sales = pd.read_pickle('./dataset/walmart_sales.pkl')

print(sales.info())


# Import NumPy and create custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)


# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))

sales_1_1 = sales[(sales['store'] == 1) & (sales['department'] == 1)]

# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values('date')

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])
