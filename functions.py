import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np
import pandas as pd

def rank_plot(data,label,top,bestworst = "best"):
    if bestworst == "best":
        data = data.sort_values(by=label,ascending=False)
        title = f"Top {top} best {label} movies"
    elif bestworst == "worst":
        data = data.sort_values(by=label,ascending=True)
        title = f"Top {top} worst {label} movies"
    color = ["blue","green","red","cyan","magenta","yellow","black","springgreen","yellowgreen","skyblue"]
    performance = np.arange(0,top,1)
    cmap = dict(zip(performance[:top], color[:top]))
    fig, ax = plt.subplots(figsize=(8,5))
    plt.bar(x=data['name'].head(top),height=data[label].head(top),color=color[:top])
    ax.set_xticklabels('')
    plt.title(title)
    plt.xlabel("Movie names")
    plt.ylabel(label)
    patches = [Patch(color=v, label=k) for k, v in cmap.items()]
    plt.legend(labels=tuple(data['name'].head(top).values),
               handles=patches,
               bbox_to_anchor=(1.0,0.5),
               loc='center left',
               borderaxespad=0,
               fontsize=7,
               frameon=False)
    plt.tight_layout()
    plt.show()

def company_stats(data,columns):
    company = pd.DataFrame(data["company"].value_counts()).reset_index()
    company = company.rename(columns={"index": "name", "company": "films_number"})
    for column in columns:
        stat = pd.DataFrame(data[["company",column]].groupby("company").sum()).reset_index()
        stat = stat.rename(columns={"company": "name"})
        company = company.merge(stat, on="name")
        company[f"mean_{column}"] = company[column] / company["films_number"]
    company = company.drop(axis=1,columns=["score","relative_revenue"])
    return company