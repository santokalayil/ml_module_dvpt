# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from prep import setView
setView()


df = pd.read_csv('risk_factors_cervical_cancer.csv', index_col = 0)
df = df.replace('?', np.NaN).copy()

from cleaning import plotNaN
plotNaN(df,(12, 12))
# 