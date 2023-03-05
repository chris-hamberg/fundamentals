import pandas as pd


def build(df):
    x = ((df["DBO (x)"]-df["DBO (x)"].mean())*(df["PL"]-df["PL"].mean())).sum()
    y = ((df["DBO (x)"]-df["DBO (x)"].mean())**2).sum()
    b = x / y

    a = df["PL"].mean() - b * df["DBO (x)"].mean()

    #y_hat = a + b * df["DBO (x)"]

    print(f"a = {a}\nb = {b}\n")


df = pd.read_csv("regression.csv", index_col=0)
print("regression.csv")
build(df)


df = pd.read_csv("regression_clean.csv", index_col=0)
print("regression_clean.csv")
build(df)
