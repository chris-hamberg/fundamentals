import matplotlib.pyplot as plt
df = []


def presiduals(plt, df):

    df.iloc[:12].plot.scatter("DBO gross", "residuals1", color="lime")
    plt.title("Yearly DBO vs. Earnings Residuals ($y - \hat{y}$) (from 2014 through 2016)")
    plt.xlabel("DBO (in tens of billions)")
    plt.ylabel("$y - \hat{y}$")
    plt.savefig("plots/residuals.2014.2016.png")
    plt.show()

    df.iloc[12:24].plot.scatter("DBO gross", "residuals2", color="magenta")
    plt.title("Yearly DBO vs. Earnings Residuals ($y - \hat{y}$) (from 2017 through 2019)")
    plt.xlabel("DBO (in tens of billions)")
    plt.ylabel("$y - \hat{y}$")
    plt.savefig("plots/residuals.2017.2019.png")
    plt.show()

    df.plot.scatter("DBO gross", "residuals3", color="red")
    plt.title("Yearly DBO vs. Earnings Residuals ($y - \hat{y}$) (from 2014 through 2022)")
    plt.xlabel("DBO (in tens of billions)")
    plt.ylabel("$y - \hat{y}$")
    plt.savefig("plots/residuals.2014.2022.png")
    plt.show()