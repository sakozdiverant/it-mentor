# -*- coding: utf-8 -*-
# Даны три числа. Найти наименьшее из них
def main():
    first_number = int(input("Введите первое число: "))
    second_number = int(input("Введите второе число: "))
    third_number = int(input("Введите третье число: "))

    smallest = first_number

    if second_number < smallest:
        smallest = second_number
    if third_number < smallest:
        smallest = third_number

    print(f"Наименьшее число: {smallest}")

if __name__ == "__main__":
    main()