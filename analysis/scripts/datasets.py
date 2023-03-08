import matplotlib.pyplot as plt
df = []

def pdatasets(plt, df):

    df.loc[:11].plot.scatter("DBO gross", "earnings", color="lime")
    plt.title("Yearly DBO vs Earnings Dataset (2014 through 2016)")
    plt.xlabel("DBO (in tens of billions)")
    plt.ylabel("Earnings (in hundreds of millions)")
    plt.savefig("plots/dataset.2014.2016.png")
    plt.show()

    df.loc[12:23].plot.scatter("DBO gross", "earnings", color="magenta")
    plt.title("Yearly DBO vs Earnings Dataset (2017 through 2019)")
    plt.xlabel("DBO (in tens of billions)")
    plt.ylabel("Earnings (in hundreds of millions)")
    plt.savefig("plots/dataset.2017.2019.png")
    plt.show()

    df.plot.scatter("DBO gross", "earnings", color="red")
    plt.title("Yearly DBO vs. Earnings Dataset (2014 through 2022)")
    plt.xlabel("DBO (in tens of billions)")
    plt.ylabel("Earnings (in hundreds of millions)")
    plt.savefig("plots/dataset.2014.2022.png")
    plt.show()