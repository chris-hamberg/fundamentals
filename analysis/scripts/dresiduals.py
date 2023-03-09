import matplotlib.pyplot as plt
df = []


def dred(plt, df):
    plt.scatter(df.x, df.residuals, color="cyan")
    plt.title("Residuals on Float Size to Price Movements")
    plt.xlabel("Residuals")
    plt.ylabel("Maximum Percentage PL on Price")
    plt.savefig("plots/dilution.price.red.png")
    plt.show()