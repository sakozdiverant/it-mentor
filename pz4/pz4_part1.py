# -*- coding: utf-8 -*-
#Даны три целых числа. Найти количество положительных чисел в исходном наборе.
def main():
    first_number = int(input("Введите первое число: "))
    second_number = int(input("Введите второе число: "))
    third_number = int(input("Введите третье число: "))

    positive_count = 0

    if first_number > 0:
        positive_count += 1
    if second_number > 0:
        positive_count += 1
    if third_number > 0:
        positive_count += 1

    print(f"Количество положительных чисел: {positive_count}")

if __name__ == "__main__":
    main()