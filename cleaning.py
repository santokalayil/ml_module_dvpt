import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plotNaN(df, figsize=(10,10)):
    """This Function  plots all the null values of the dataframe provided within the argument..

    Args:
        df (pandas.DataFrame): Table like structure provided for Data Analysis
        figsize (tuple, optional): Figure size of Matplotlib.pyplot. Defaults to (10,10).
    """    
    plt.figure(figsize=figsize)
    ( (df.isnull().sum() / df.shape[0]) * 100 ).sort_values().plot(kind='barh')
    plt.show()