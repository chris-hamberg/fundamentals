import matplotlib.pyplot as plt
import pandas as pd


df = pd.DataFrame([])


kwargs = {"colors": ["lime", "darkviolet"], "labels": []} 
labels = ["Postive Quarters", "Negative Quarters"]
title  = "Positive vs Negative Quarters "


def _periods(df): 
    return [
        ((2014, 2016), len(df.loc[:11][df.loc[:11].earnings > 0])     / len(df.loc[:11])),
        ((2017, 2019), len(df.loc[11:23][df.loc[11:23].earnings > 0]) / len(df.loc[11:23])),
        #((2020, 2022), len(df.loc[24:][df.loc[24:].earnings > 0])   / len(df.loc[24:])),
        ((2017, 2022), len(df.loc[11:][df.loc[11:].earnings > 0])     / len(df.loc[11:])),
        #((2014, 2022), len(df[df.earnings > 0])                     / len(df))
            ]

def epies(plt, df):
    periods = _periods(df)
    for p in periods:
        positive = p[1]
        negative = 1 - p[1]
        kwargs["labels"] = [f"{positive * 100:,.1f}%", f"{negative * 100:,.1f}%"]
        plt.pie([positive, negative], **kwargs)
        plt.title(title + f"({p[0][0]} through {p[0][1]})")
        plt.legend(labels)
        plt.savefig(f"plots/epie.{p[0][0]}.{p[0][1]}.png")
        plt.show()
