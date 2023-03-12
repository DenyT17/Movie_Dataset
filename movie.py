import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
data = pd.read_csv("movies.csv")

# Dropping or filling nan value.
data["score"].fillna(value=data["score"].mean(),inplace=True)
data["runtime"].fillna(value=data["runtime"].mean(),inplace=True)
data["score"].fillna(value=data["gross"].mean(),inplace=True)
data["votes"].fillna(value=data["votes"].mean(),inplace=True)
data["gross"].fillna(value=data["gross"].mean(),inplace=True)
data["budget"].fillna(value=data["budget"].mean(),inplace=True)
data["rating"].fillna(value="Unknown",inplace=True)
data = data.dropna(subset=["genre","writer","country","star","country","company"])


# Data Visualisation
