# -*- coding: utf-8 -*-
#Найти факториалы чисел от 1 до 5 (включительно).

import math

def main():
    [print(f"Факториал {i} = {math.factorial(i)}") for i in range(1, 6)]

if __name__ == "__main__":
    main()
