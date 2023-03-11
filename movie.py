import pandas as pd
import numpy as np
import seaborn as sn

pd.set_option('display.max_columns', None)
data = pd.read_csv('movies.csv')

# Sorting value by movie name
data = data.sort_values(by=["MOVIES"])
# Drop duplicate+
data = data.drop_duplicates(subset=["MOVIES"])
# Drop NAN value from YEAR columns
data.dropna(subset=["YEAR"],inplace=True)
# Creating two dataframe, first contain only serials and second contain only movies
serial = data.loc[(data['YEAR'].str.contains("–"))].reset_index(drop=True)
movie = data.loc[(~data["YEAR"].str.contains("–"))].reset_index(drop=True)
print(serial)
print(movie)

