# -*- coding: utf-8 -*-
#Даны два числа. Вывести большее из них.
def main():
    first_number = int(input("Введите первое число: "))
    second_number = int(input("Введите второе число: "))
    #third_number = int(input("Введите третье число: "))

    if first_number > second_number:
        print(f"Большее число: {first_number}")
    else:
        print(f"Большее число: {second_number}")

if __name__ == "__main__":
    main()