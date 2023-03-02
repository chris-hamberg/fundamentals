import matplotlib.pyplot as plt
import pandas as pd


def plot(df):
    plt.scatter(df["DBO (x)"], df["PL"], color="black")
    plt.plot(df["DBO (x)"], df["y_hat = a + bx"], color="red")
    plt.xlabel("DBO (in billions)")
    plt.ylabel("net loss (profit) (in billions)")
    plt.title("DBO PL Determinate Regression Line")
    plt.show()


df = pd.read_csv("regression.csv", index_col=0)
plot(df)

input()

df = pd.read_csv("regression_clean.csv", index_col=0)
plot(df)
