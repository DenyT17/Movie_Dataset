import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
data = pd.read_csv('movies.csv')
# Sorting value by movie name
data = data.sort_values(by=["MOVIES"])
data = data.rename(columns={"MOVIES":"Name",
                     "YEAR":"Year/s_of_creation",
                     "GENRE":"Genre",
                     "RATING":"Rating",
                     "ONE-LINE":"Description",
                     "STARS":"Stars",
                     "VOTES":"Number_of_votes",
                     })
# Drop NAN value from YEAR columns
data.dropna(subset=["Year/s_of_creation","Rating","RunTime"],inplace=True)
data["Number_of_votes"] = data["Number_of_votes"].apply(lambda x: int(x.replace(",","")))
# Creating two dataframe, first contain only serials and second contain only movies
serial = data.loc[(data["Year/s_of_creation"].str.contains("–"))].reset_index(drop=True)
movie = data.loc[(~data["Year/s_of_creation"].str.contains("–"))].reset_index(drop=True)

# Number of episodes
episodes = pd.DataFrame(serial["Name"].value_counts().reset_index())
episodes = episodes.rename(columns={"index":"Name",
                                    "Name":"Number_of_episodes"})

mean_rating = pd.DataFrame(serial[["Name","Rating","Number_of_votes"]])
mean_rating["Mean"] = mean_rating["Rating"] * mean_rating["Number_of_votes"]
serial = serial.drop_duplicates(subset="Name")
serial = serial.merge(episodes,on="Name")
serial = serial.drop(["Gross",],axis=1)

mean_rating = mean_rating.groupby("Name").sum()
mean_rating["Rating"] = mean_rating["Mean"]/mean_rating["Number_of_votes"]
print(mean_rating)




