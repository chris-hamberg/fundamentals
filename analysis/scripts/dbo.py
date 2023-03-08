import matplotlib.pyplot as plt
import pandas as pd


df = pd.DataFrame([])


def dplot(plt, df):
    dbo = df.loc[:23].groupby("year").agg("sum")
    ax = plt.axes()
    plt.plot(dbo.index, dbo["DBO gross"], color="lime")
    plt.scatter([2015], [1.17 * 10 ** 10], color="red", linewidth=3.0, edgecolor="red")
    ax.annotate("", xytext=(2015.25, 1.04 * 10 ** 10), xy=(2018.5, 1.115 * 10 ** 10), 
                arrowprops={"color": "darkviolet", "width": 1,
                            "headwidth": 15, "headlength": 15})
    ax.set_xticks([2014, 2015, 2016, 2017, 2018, 2019])
    ax.set_xticklabels([2015, 2016, 2017, 2018, 2019, 2020])
    plt.xlabel("Year")
    plt.ylabel("DBO (in tens of billions)")
    plt.title("Domestic Box Office (2014 through 2019)")
    plt.grid(True, alpha = 0.2)
    plt.savefig("plots/dbo.2014.2019.png")
    plt.show()