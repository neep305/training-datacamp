import pandas as pd

"""
Source: SILSO, Daily total sunsport number
(http://www.sidc.be/silso/infossntotdaily)
Filename: ISSN_D_tot.csv
Format: Comma Separated values (adapted for import e.g. in MS Excel)

Contents:
Column 1-3: Gregorian calendar date
 - Year
 - Month
 - Day
Column 4: Date in fraction of year
Column 3: Daily total sunspot number. A value of -1 indicates that no number is available for that day (missing value).
Column 4: Definitive/provisional indicator. '1' indicates that the value is definitive. '0' indicates that the value is still provisional and is subject to a possible revision (Usually the last 2 or 3 months)
"""
sunspots = pd.read_csv('./dataset/ISSN_D_tot.csv')
# sunspots.info()

print(sunspots.iloc[10:20, :])