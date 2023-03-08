import pandas as pd
import numpy as np
import df2img


def comparative_build(a1, a2, a3, b1, b2, b3):

    clean = lambda v: f"{v:,.0f}"

    X  = list(range(9600000000, 12500000000, 250000000))
    Y1 = pd.Series([a1 + b1 * x for x in X])
    Y2 = pd.Series([a2 + b2 * x for x in X])
    Y3 = pd.Series([a3 + b3 * x for x in X])
    X  = [clean(x) for x in X]

    mY1 = Y1.mean(), Y1.min(), Y1.max()
    mY2 = Y2.mean(), Y2.min(), Y2.max()
    mY3 = Y3.mean(), Y3.min(), Y3.max()

    Y1 = [clean(y) for y in Y1]
    Y2 = [clean(y) for y in Y2]
    Y3 = [clean(y) for y in Y3] 

    columns = ["DBO", "Earnings (2014 - 2016)", "Earnings (2017 - 2019)", "Earnings (2014 - 2022)"]

    predictions = pd.DataFrame(np.array([X, Y1, Y2, Y3]).T, columns = columns)

    return predictions, mY1, mY2, mY3


def comparative_draw(predictions):

    bg   = "#333333"
    font = "Arial"

    fig = df2img.plot_dataframe(predictions,

        title={"text": "All Predictions", "font_color": "purple", "font_size": 32, 
            "font_family": font, "x": 0.41, "yanchor": "middle"},
        
        tbl_header = {"align": "center", "fill_color": bg, "font_color": "darkviolet", 
                    "font_size": 20, "line": {"color": bg}, "font_family": font},
            
        tbl_cells = {"align": "center", "fill_color": bg, "font_color": "cyan", 
                    "font_size": 16, "line": {"color": bg}, "height": 28, "font_family": font},
                    row_fill_color = (bg, "purple"),
        
        print_index = False,
        paper_bgcolor = bg,
        fig_size = (1000, 420),
        col_width = 6)

    df2img.save_dataframe(fig = fig, filename = "dataframes/all.predictions.png")


def comparative(a1, a2, a3, b1, b2, b3):
    predictions, mY1, mY2, mY3 = comparative_build(a1, a2, a3, b1, b2, b3)
    comparative_draw(predictions)
    return mY1, mY2, mY3