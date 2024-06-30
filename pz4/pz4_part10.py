# -*- coding: utf-8 -*-
# *** Реализуйте программу калькулятор. На вход подается три значения:
# первое число, второе число и Дано целое число в диапазоне 100–999.
# Вывести строку-описание данного числа, например: 256 — «двести пятьдесят шесть»,
# 814 — «восемьсот четырнадцать».
# операция( *, /, + или -) . На выходе должны получить число, после выполнения операции.

def number_to_words(num):
    hundreds = {
        1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста',
        5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот', 9: 'девятьсот'
    }

    tens = {
        2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят',
        6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'
    }

    teens = {
        10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
        14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
        17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'
    }

    units = {
        1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
        6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'
    }

    if not (100 <= num <= 999):
        return "Число должно быть в диапазоне от 100 до 999"

    h = num // 100
    t = (num // 10) % 10
    u = num % 10

    words = []

    if h in hundreds:
        words.append(hundreds[h])

    if t == 1:
        words.append(teens[t * 10 + u])
    else:
        if t in tens:
            words.append(tens[t])
        if u in units:
            words.append(units[u])

    return " ".join(words)

def calculator():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        operation = input("Введите операцию (*, /, +, -): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Ошибка: деление на ноль"
        else:
            return "Ошибка: недопустимая операция"

        return f"Результат: {result}"
    except ValueError:
        return "Ошибка: введите допустимые числа"


def main():
    while True:
        print("\nВыберите опцию:")
        print("1. Описание числа")
        print("2. Калькулятор")
        print("3. Выход")

        first_number = input("Введите номер опции: ")

        if first_number == '1':
            try:
                num = int(input("Введите число в диапазоне 100–999: "))
                print(f"{num} — «{number_to_words(num)}»")
            except ValueError:
                print("Ошибка: Введите число в диапазоне 100–999")
                continue

        elif first_number == '2':
            print(calculator())
        elif first_number == '3':
            break
        else:
            print("Неверный выбор, попробуйте еще раз.")

if __name__ == "__main__":
    main()