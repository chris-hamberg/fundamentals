def coefficient(c1, c2, df):
    return (df[c1] * df[c2]).sum() / (len(df)-1)
