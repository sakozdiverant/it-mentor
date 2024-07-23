# -*- coding: utf-8 -*-
#

import pandas as pd

def main():
    df = pd.read_csv("bikes.csv", header=0)

    print(f"Сумма столбца Rachel1: {sum(df['Rachel1'])}")

    print(df['Rachel1'].value_counts())

if __name__ == '__main__':
    main()