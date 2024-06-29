# -*- coding: utf-8 -*-
# Дан номер месяца — целое число в диапазоне 1–12 (1 — январь, 2 — февраль и т. д.).
# Определить количество дней в этом месяце для невисокосного года.
def main():
    first_number = int(input("Введите номер месяца (1-12): "))
    # second_number = int(input("Введите координату Y: "))
    # third_number = int(input("Введите третье число: "))5

    if first_number in [1, 3, 5, 7, 8, 10, 12]:
        print("31 день")
    elif first_number in [4, 6, 9, 11]:
        print("30 дней")
    elif first_number == 2:
        print("28 дней")
    else:
        print("ошибка")

if __name__ == "__main__":
    main()