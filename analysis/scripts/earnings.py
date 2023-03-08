import matplotlib.pyplot as plt
import pandas as pd


df = pd.DataFrame([])


def eplot(i, start, end, xtext, ytext, x, y, e, plt, df):
    
    years = list(range(2014, 2023))
    
    ax = plt.axes()

    plt.plot(years[:i],  df.groupby("year").agg(["sum"])[:end]["earnings"])

    plt.plot(years[:i], 
            [df.groupby("year").agg(["sum"])[:2016]["earnings"].mean()] * i, 
            color="lime", 
            alpha = 0.8, linestyle="--")

    plt.plot(years[:i], 
            [df.groupby("year").agg(["sum"])[2017:2019]["earnings"].mean()] * i, 
            color="red", 
            alpha = 0.7, linestyle="--")

    if (end == 2022):
        plt.plot(years, 
            [df.groupby("year").agg(["sum"])[2017:]["earnings"].mean()] * i, 
                         color="red")

    plt.scatter([2015], [0], color="red", linewidth=3.0, edgecolor="red")

    plt.annotate("Adam becomes CEO", xy=[x, y * 10**e], 
            xytext=[xtext, ytext * 10**e], 
            arrowprops={
                "facecolor":"red", "arrowstyle":"->", "connectionstyle":"arc3"
                })


    legend = ["Earnings", "Mean Earnings (2014 through 2016)", 
              "Mean Earnings (2017 through 2019)"]
    if (end == 2022):
        legend.append("Mean Earnings (2017 through 2022)")

    plt.legend(legend)

    plt.grid(True, alpha = 0.2)
    plt.title(f"AMC Yearly Earnings from {start} through {end}")
    plt.xlabel("Year")
    plt.ylabel("Earnings (in hundreds of millions)")
    ax.set_xticks(list(range(start, end+1)))
    ax.set_xticklabels([str(x + 1) for x in range(start, end+1)])
    plt.savefig(f"plots/earnings.{start}.{end}.png")
    plt.show()
