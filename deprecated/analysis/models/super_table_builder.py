import pandas as pd
import numpy as np
import os

def build():
    fname1 = os.path.join("estimate_revenue_from_DBO",     "predictor.csv")
    fname2 = os.path.join("predict_earnings_from_DBO",     "predictor.csv")
    fname3 = os.path.join("predict_revenue_from_DBO",      "predictor.csv")
    fname4 = os.path.join("predict_earnings_from_revenue", "predictor.csv")

    M1 = pd.read_csv(fname1, index_col=0)
    M2 = pd.read_csv(fname3, index_col=0)
    M3 = pd.read_csv(fname4, index_col=0)
    M4 = pd.read_csv(fname2, index_col=0)

    rssdM2 = 74878802.26825552
    rssdM3 = 128006839.0372937
    rssdM4 = 111259102.882163

    X = synthetic_DBO = np.array(list(range(7000000000, 13500000000, 
        500000000)))

    sM1 = market_share       = M1.loc[2014]["Market Share"]
    rM1 = percent_of_revenue = M1.loc[2014]["tRev avg percent"] * 100

    predictM1 = lambda x: ((x * sM1) / rM1) * 100
    predictM2 = lambda x: 4 * (M2.loc[12]["a"] + M2.loc[12]["b"] * (x / 4))
    predictM3 = lambda x: 4 * (M3.loc[12]["a"] + M3.loc[12]["b"] * (x / 4))
    predictM4 = lambda x: 4 * (M4.loc[0]["a"]  + M4.loc[0]["b"]  * (x / 4))

    columns = [
        "DBO",
        "DBO -> revenue (Model 1)",
        "revenue -(2 rssd)",
        "revenue -rssd",
        "revenue",
        "revenue +rssd",
        "revenue +(2 rssd)",
        "revenue -> earnings -(2 rssd)",
        "earnings -rssd",
        "earnings",
        "earnings +rssd",
        "earnings +(2 rssd)",
        "DBO -> earnings -(2 rssd)",
        "earnings -rssd (Model 4)",
        "earnings (Model 4)",
        "earnings +rssd (Model 4)",
        "earnings +(2 rssd) (Model 4)"]


    y_M1, y_M2, y_M3, y_M4 = [], [], [], []
    for x in X:
        y_M1.append(predictM1(x))
        y2 = predictM2(x)
        y_M2.append(y2)
        y_M3.append(predictM3(y2))
        y_M4.append(predictM4(x))

    y_M1, y_M2 = np.array(y_M1), np.array(y_M2)
    y_M3, y_M4 = np.array(y_M3), np.array(y_M4)

    df = pd.DataFrame(np.array([
            X,
            y_M1,
            y_M2 - (2 * rssdM2),
            y_M2 - rssdM2,
            y_M2,
            y_M2 + rssdM2,
            y_M2 + (2 * rssdM2),
            y_M3 - (2 * rssdM3),
            y_M3 - rssdM3,
            y_M3,
            y_M3 + rssdM3,
            y_M3 + (2 * rssdM3),
            y_M4 - (2 * rssdM4),
            y_M4 - rssdM4,
            y_M4,
            y_M4 + rssdM4,
            y_M4 + (2 * rssdM4)]).T,

            columns = columns)

    return df
