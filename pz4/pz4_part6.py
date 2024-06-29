# -*- coding: utf-8 -*-
# Дано целое число K. Вывести строку-описание оценки, соответствующей числу K
# (1 — «плохо», 2 — «неудовлетворительно», 3 — «удовлетворительно», 4 — «хорошо», 5 — «отлично»).
# Если K не лежит в диапазоне 1–5, то вывести строку «ошибка».
def main():
    first_number = int(input("Введите оценку K (1-5): "))
    # second_number = int(input("Введите координату Y: "))
    # third_number = int(input("Введите третье число: "))

    if first_number == 1:
        print("плохо")
    elif first_number == 2:
        print("неудовлетворительно")
    elif first_number == 3:
        print("удовлетворительно")
    elif first_number == 4:
        print("хорошо")
    elif first_number == 5:
        print("отлично")
    else:
        print("ошибка")

if __name__ == "__main__":
    main()