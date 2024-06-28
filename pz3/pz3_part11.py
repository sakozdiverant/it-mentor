# -*- coding: utf-8 -*-
#Найти факториалы чисел от 1 до 5 (включительно).

import math

def main():
    for i in range(1, 6):
        factorial = math.factorial(i)
        print(f"Факториал {i} = {factorial}")

if __name__ == "__main__":
    main()
