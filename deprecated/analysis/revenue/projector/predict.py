import pandas as pd


df = pd.read_csv("projector.csv", index_col=0)
df = df.drop(2014)
df = df.drop(2015)
df = df.drop(2016)
print(df)

def p(DBO):

    market_share = df.loc[2017]["Market Share"]
    percent_revenue = df.loc[2017]["tRev avg percent"] * 100

    market_share = DBO * market_share

    return (market_share / percent_revenue) * 100
