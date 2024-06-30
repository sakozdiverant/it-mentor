# -*- coding: utf-8 -*-
# Даны два целых числа: D (день) и M (месяц), определяющие правильную дату невисокосного года.
# Вывести значения D и M для даты, следующей за указанной.
def main():
    first_number = int(input("Введите месяц (1-12): "))
    second_number = int(input("Введите день (1-31): "))
    # third_number = int(input("Введите третье число: "))

    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    if first_number in days_in_month:
        if second_number < days_in_month[first_number]:
            second_number += 1
        elif second_number > days_in_month[first_number]:
            print(f"Ошибка: В {first_number} месяце количество дней {days_in_month[first_number]}")
        else:
            second_number = 1
            first_number += 1
            if first_number > 12:
                first_number = 1
        print(f"Следующая дата: День {second_number} месяц {first_number}")
    else:
        print("Ошибка")

if __name__ == "__main__":
    main()