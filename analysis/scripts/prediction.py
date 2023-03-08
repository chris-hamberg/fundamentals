import pandas as pd
import numpy as np
import df2img


def prediction_build(a3, b3, r3, df):

    clean   = lambda v: f"{v:,.0f}"
    minimum = int(max(df["DBO gross"].min(), 7500000000))
    maximum = int(df["DBO gross"].max())

    inc = 500000000

    X = list(range(minimum, maximum + inc, inc))
    Y = pd.Series([a3 + b3 * x for x in X])

    DBO      = X
    Lowest   = Y - (2 * r3)
    Low      = Y - r3
    Earnings = Y
    High     = Y + r3
    Highest  = Y + (2 * r3)

    DBO      = [clean(x) for x in DBO]
    Lowest   = [clean(s) for s in Lowest]
    Low      = [clean(s) for s in Low]
    Earnings = [clean(y) for y in Earnings]
    High     = [clean(s) for s in High]
    Highest  = [clean(s) for s in Highest]

    columns = ["DBO", "Lowest", "Low", "Earnings", "High", "Highest"]

    prediction = pd.DataFrame(np.array([DBO, Lowest, Low, Earnings, High, Highest]).T,
                            columns = columns)
    return prediction


def prediction_draw(prediction):
    bg   = "#333333"
    font = "Arial"

    fig = df2img.plot_dataframe(prediction,

        title={"text": "2023 Earnings from DBO Prediction", "font_color": "purple", "font_size": 32, 
            "font_family": font, "x": 0.25, "yanchor": "middle"},
        
        tbl_header = {"align": "center", "fill_color": bg, "font_color": "darkviolet", 
                    "font_size": 20, "line": {"color": bg}, "font_family": font},
            
        tbl_cells = {"align": "center", "fill_color": bg, "font_color": "cyan", 
                    "font_size": 16, "line": {"color": bg}, "height": 28, "font_family": font},
                    row_fill_color = (bg, "purple"),
        
        print_index = False,
        paper_bgcolor = bg,
        fig_size = (1000, 450),
        col_width = 6)

    df2img.save_dataframe(fig = fig, filename = "dataframes/2023.prediction.png")


def predict(a3, b3, r3, df):
    prediction = prediction_build(a3, b3, r3, df)
    prediction_draw(prediction)