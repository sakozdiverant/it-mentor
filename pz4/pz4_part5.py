# -*- coding: utf-8 -*-
# Даны координаты точки, не лежащей на координатных осях OX и OY.
# Определить номер координатной четверти, в которой находится данная точка.
# Координаты задаются пользователем, например (10, 15).
def main():
    first_number = int(input("Введите координату X: "))
    second_number = int(input("Введите координату Y: "))
    # third_number = int(input("Введите третье число: "))

    if first_number > 0 and second_number > 0:
        print("Точка находится в первой четверти")
    elif first_number < 0 and second_number > 0:
        print("Точка находится во второй четверти")
    elif first_number < 0 and second_number < 0:
        print("Точка находится в третьей четверти")
    elif first_number > 0 and second_number < 0:
        print("Точка находится в четвертой четверти")

if __name__ == "__main__":
    main()