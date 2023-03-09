import matplotlib.pyplot as plt
df = []


def hplot(plt, df):
    plt.plot(df["date"], df["high"], linestyle="--", color="darkviolet", alpha=0.5)
    plt.scatter(df["date"], df["dilution"], marker="^", color="red", edgecolors="yellow")
    plt.xlabel("Date")
    plt.ylabel("Share Price")
    plt.title("History of Dilution Events (from 2016 through 2022)")
    plt.grid(True, alpha=0.2)
    plt.legend(["Daily High", "Dilution Event"])
    plt.savefig("plots/dilution.hist.png")
    plt.show()