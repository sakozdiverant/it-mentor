# -*- coding: utf-8 -*-
# Дан номер месяца — целое число в диапазоне 1–12 (1 — январь, 2 — февраль и т. д.).
# Определить количество дней в этом месяце для невисокосного года.

def days_in_month(month):
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            return 28
        case _:
            return "ошибка"


def main():
    first_number = int(input("Введите номер месяца (1-12): "))
    print(days_in_month(first_number))

if __name__ == "__main__":
    main()