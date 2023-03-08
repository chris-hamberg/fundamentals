import matplotlib.pyplot as plt
df = []

def rplot(x, y_hat1, y_hat2, y_hat3, plt, df):
    df.iloc[:12].plot.scatter("DBO gross", "earnings", alpha = 0.9, color="lime")
    plt.plot(x.iloc[:12], y_hat1, linewidth=1.5, color = "cyan")
    plt.title("Linear Regression Yearly DBO vs. Earnings (from 2014 through 2016)")
    plt.xlabel("DBO (in tens of billions)")
    plt.ylabel("Earnings (in billions)")
    plt.savefig("plots/regression.2014.2016.png")
    plt.show()

    df.iloc[12:24].plot.scatter("DBO gross", "earnings", alpha = 0.9, color="magenta")
    plt.plot(x.iloc[12:24], y_hat2, linewidth=1.5, color = "cyan")
    plt.title("Linear Regression Yearly DBO vs. Earnings (from 2017 through 2019)")
    plt.xlabel("DBO (in tens of billions)")
    plt.ylabel("Earnings (in billions)")
    plt.savefig("plots/regression.2017.2019.png")
    plt.show()

    df.plot.scatter("DBO gross", "earnings", alpha = 0.9, color="red")
    plt.plot(x, y_hat3, linewidth=1.5, color = "cyan")
    plt.title("Linear Regression Yearly DBO vs. Earnings (from 2014 through 2022)")
    plt.xlabel("DBO (in tens of billions)")
    plt.ylabel("Earnings (in billions)")
    plt.savefig("plots/regression.2014.2022.png")
    plt.show()