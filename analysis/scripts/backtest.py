import matplotlib.pyplot as plt
df = []


def backtest(a3, b3, plt, df):
    df["y_hat"] = a3 + b3 * df["DBO gross"]
    plt.plot(df.index, df.y_hat, color="lime")
    plt.plot(df.index, df.earnings, color="darkviolet")
    plt.legend(["Predicted Earnings", "Actual Earnings"], loc=3)
    plt.title("Earnings Prediction Back Test")
    plt.xlabel("Year")
    plt.ylabel("Yearly Earnings (in billion)")
    plt.grid(True, alpha = 0.2)
    plt.savefig("plots/backtest.png")
    plt.show()