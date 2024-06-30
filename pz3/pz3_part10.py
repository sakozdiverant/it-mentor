# -*- coding: utf-8 -*-
# Вывести значения функции y=x^2 от 1 до 10 с шагом 0.5.
import numpy as np
def main():
    [print(f"y = {x}^2 = {x ** 2}") for x in np.arange(1, 10, 0.5)]

if __name__ == "__main__":
    main()
