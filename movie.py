import matplotlib.pyplot as plt
import pandas as pd
from functions import rank_plot,company_stats

pd.set_option('display.max_columns', None)
data = pd.read_csv("movies.csv")


# Dropping or filling nan value.
data["score"].fillna(value=data["score"].mean(),inplace=True)
data["runtime"].fillna(value=data["runtime"].mean(),inplace=True)
data["score"].fillna(value=data["gross"].mean(),inplace=True)
data["votes"].fillna(value=data["votes"].mean(),inplace=True)
data["rating"].fillna(value="Unknown",inplace=True)
data = data.dropna(subset=["genre","writer","country","star","country","company","budget","gross"])


# Creating new columns / dataframe
genre = pd.DataFrame(data['genre'].value_counts())
other_gener = genre.loc[genre["genre"] < 300].sum().values
genre = genre.drop(genre[genre["genre"] < 300].index).reset_index()
genre.loc[len(genre.index)] = ["Other", other_gener[0]]

data["relative_revenue"] = data["gross"] / data["budget"]

company = company_stats(data,["gross","budget","score","runtime","relative_revenue"])

## Data Visualisation

rank_plot(data,"budget",10)
rank_plot(data,"score",5)
rank_plot(data,"gross",10)
rank_plot(data,"relative_revenue",10)

rank_plot(data,"budget",10,"worst")
rank_plot(data,"score",5,"worst")
rank_plot(data,"gross",10,"worst")
rank_plot(data,"relative_revenue",10,"worst")

rank_plot(company,"budget",10)
rank_plot(company,"mean_score",5)
rank_plot(company,"gross",10)
rank_plot(company,"mean_relative_revenue",10)

fig, ax = plt.subplots(figsize=(8, 5))
plt.pie(genre["genre"],labels=genre["index"],autopct='%1.0f%%')
plt.title("The most popular genres")
plt.show()

