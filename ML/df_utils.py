
def col_in_df(df, col):
	if col in df.columns:
		return True
	else:
		return False

def rm_col(df, col):
    if col_in_df(df, col):
        df.drop(col, axis=1, inplace=True)
    return df

def isDF(df):
    from pandas.core.frame import DataFrame as pddf
    return isinstance(c.Data.DataFrame, pddf)