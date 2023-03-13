import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np

def top_plot(data,label,top):
    color = ["blue","green","red","cyan","magenta","yellow","black","springgreen","yellowgreen","skyblue"]
    performance = np.arange(0,top,1)
    cmap = dict(zip(performance[:top], color[:top]))
    fig, ax = plt.subplots(figsize=(8,5))
    data = data.sort_values(by=label,ascending=False)
    plt.bar(x=data['name'].head(top),height=data[label].head(top),color=color[:top])
    ax.set_xticklabels('')
    plt.title(f"Top {top} {label} movies")
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