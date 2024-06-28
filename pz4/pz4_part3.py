# -*- coding: utf-8 -*-
#Даны два числа. Вывести вначале большее, а затем меньшее из них.
def main():
    first_number = int(input("Введите первое число: "))
    second_number = int(input("Введите второе число: "))
    #third_number = int(input("Введите третье число: "))

    if first_number > second_number:
        print(f"Большее: {first_number}, Меньшее: {second_number}")
    else:
        print(f"Большее: {second_number}, Меньшее: {first_number}")

if __name__ == "__main__":
    main()