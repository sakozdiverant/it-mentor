# -*- coding: utf-8 -*-
# Дано целое число K. Вывести строку-описание оценки, соответствующей числу K
# (1 — «плохо», 2 — «неудовлетворительно», 3 — «удовлетворительно», 4 — «хорошо», 5 — «отлично»).
# Если K не лежит в диапазоне 1–5, то вывести строку «ошибка».

def grade_description(k):
    match k:
        case 1:
            return "плохо"
        case 2:
            return "неудовлетворительно"
        case 3:
            return "удовлетворительно"
        case 4:
            return "хорошо"
        case 5:
            return "отлично"
        case _:
            return "ошибка"

def main():
    first_number = int(input("Введите оценку K (1-5): "))
    print(grade_description(first_number))


if __name__ == "__main__":
    main()