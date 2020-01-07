import pandas as pd


def rename_cols(columns):
    result = list(map(lambda x: x.lower().replace(' ', '_'), columns))

    return result
"""
# Create list of columns to use
cols = ["zipcode","agi_stub","mars1","MARS2","NUMDEP"]

# Create data frame from csv using only selected columns
data = pd.read_csv("vt_tax_data_2016.csv", usecols=cols)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())
"""
data_with_none = pd.read_csv('./dataset/walmart_prd_details.csv', sep=',', nrows=0)

print(rename_cols(list(data_with_none)))

data_with_new_cols = pd.read_csv('./dataset/walmart_prd_details.csv',
                                 sep=',',
                                 skiprows=1,
                                 names=rename_cols(list(data_with_none)))

print(data_with_new_cols)
