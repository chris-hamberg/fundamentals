import matplotlib.pyplot as plt
df = []


def dilute(plt, df, color, fname):
    plt.scatter(df.x, df.y, color=color)
    plt.title("Change in Float Size vs. 15-day Highest Price")
    plt.xlabel("Percentage of Float Change")
    plt.ylabel("Highest 15-day Percentage Change in Share Price")
    plt.savefig(f"plots/dilution.price.{fname}.png")
    plt.show()