# -*- coding: utf-8 -*-
#

import pandas as pd

df = pd.read_csv("bikes.csv", header=None, nrows=20, skiprows=range(0, 15), sep=",")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
print(df)
print(df.columns)
