# -*- coding: utf-8 -*-
# Вывести значения функции y=x^2 от 1 до 10 с шагом 0.5.
import numpy as np
def main():
    for x in np.arange(1, 10, 0.5):
        y = x ** 2
        print(f"y = {x}^2 = {y}")

if __name__ == "__main__":
    main()
