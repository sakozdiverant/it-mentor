# -*- coding: utf-8 -*-
# *** Реализуйте программу калькулятор. На вход подается три значения:
# первое число, второе число и Дано целое число в диапазоне 100–999.
# Вывести строку-описание данного числа, например: 256 — «двести пятьдесят шесть»,
# 814 — «восемьсот четырнадцать».
# операция( *, /, + или -) . На выходе должны получить число, после выполнения операции.

def number_to_words(num):
    if not (100 <= num <= 999):
        return "Число должно быть в диапазоне от 100 до 999"

    h = num // 100
    t = (num // 10) % 10
    u = num % 10

    words = []

    match h:
        case 1:
            words.append('сто')
        case 2:
            words.append('двести')
        case 3:
            words.append('триста')
        case 4:
            words.append('четыреста')
        case 5:
            words.append('пятьсот')
        case 6:
            words.append('шестьсот')
        case 7:
            words.append('семьсот')
        case 8:
            words.append('восемьсот')
        case 9:
            words.append('девятьсот')

    if t == 1:
        match t * 10 + u:
            case 10:
                words.append('десять')
            case 11:
                words.append('одиннадцать')
            case 12:
                words.append('двенадцать')
            case 13:
                words.append('тринадцать')
            case 14:
                words.append('четырнадцать')
            case 15:
                words.append('пятнадцать')
            case 16:
                words.append('шестнадцать')
            case 17:
                words.append('семнадцать')
            case 18:
                words.append('восемнадцать')
            case 19:
                words.append('девятнадцать')
    else:
        match t:
            case 2:
                words.append('двадцать')
            case 3:
                words.append('тридцать')
            case 4:
                words.append('сорок')
            case 5:
                words.append('пятьдесят')
            case 6:
                words.append('шестьдесят')
            case 7:
                words.append('семьдесят')
            case 8:
                words.append('восемьдесят')
            case 9:
                words.append('девяносто')

        match u:
            case 1:
                words.append('один')
            case 2:
                words.append('два')
            case 3:
                words.append('три')
            case 4:
                words.append('четыре')
            case 5:
                words.append('пять')
            case 6:
                words.append('шесть')
            case 7:
                words.append('семь')
            case 8:
                words.append('восемь')
            case 9:
                words.append('девять')

    return " ".join(words)

def calculator():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        operation = input("Введите операцию (*, /, +, -): ")

        match operation:
            case '+':
                result = num1 + num2
            case '-':
                result = num1 - num2
            case '*':
                result = num1 * num2
            case '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    return "Ошибка: деление на ноль"
            case _:
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
