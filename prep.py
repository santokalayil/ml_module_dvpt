import numpy as np
import pandas as pd
import warnings

def setView(max_rows=500,max_cols=500):
    """A function that sets jupyter enviroment to view more data and thus makes it more data science friendly.. It sets numpy print options and sets pandas max rows and cols to 500 and filters warnings. and sets random seed also.
    Args:
        max_rows (int, optional): display.max_rows of pandas. Defaults to 500.
        max_cols (int, optional): display.max_columns of pandas. Defaults to 500.
    """    
    pd.set_option('display.max_rows',max_rows)
    pd.set_option('display.max_columns',max_cols)
    np.set_printoptions(precision=3)
    pd.set_option('display.float_format', lambda x: '%.3f' % x)
    np.random.seed(8)
    import warnings
    warnings.filterwarnings('ignore')

def widen():
    """This function sets the width of jupyter notebook to 100% and thus helps to show more data in the ipynb notebook.
    """
    from IPython.core.display import display, HTML
    display(HTML("<style>.container { width:100% !important; }</style>"))