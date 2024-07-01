# -*- coding: utf-8 -*-
# Даны два целых числа: D (день) и M (месяц), определяющие правильную дату невисокосного года.
# Вывести значения D и M для даты, следующей за указанной.
def main():
    first_number = int(input("Введите месяц (1-12): "))
    second_number = int(input("Введите день (1-31): "))

    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    match first_number:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            if second_number < days_in_month[first_number]:
                second_number += 1
            elif second_number > days_in_month[first_number]:
                print(f"Ошибка: В {first_number} месяце количество дней {days_in_month[first_number]}")
                return
            else:
                second_number = 1
                first_number += 1
                if first_number > 12:
                    first_number = 1

        case 4 | 6 | 9 | 11:
            if second_number < days_in_month[first_number]:
                second_number += 1
            elif second_number > days_in_month[first_number]:
                print(f"Ошибка: В {first_number} месяце количество дней {days_in_month[first_number]}")
                return
            else:
                second_number = 1
                first_number += 1

        case 2:
            if second_number < days_in_month[first_number]:
                second_number += 1
            elif second_number > days_in_month[first_number]:
                print(f"Ошибка: В феврале количество дней {days_in_month[first_number]}")
                return
            else:
                second_number = 1
                first_number += 1

        case _:
            print("Ошибка: Неверный месяц")
            return

    print(f"Следующая дата: День {second_number} месяц {first_number}")

if __name__ == "__main__":
    main()
