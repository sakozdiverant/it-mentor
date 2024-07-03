# -*- coding: utf-8 -*-
#

import pandas as pd

df = pd.read_csv("bikes.csv", header=0)

print(f"Сумма столбца Rachel1: {sum(df['Rachel1'])}")

print(df['Rachel1'].value_counts())