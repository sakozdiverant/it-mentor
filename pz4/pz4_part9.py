# -*- coding: utf-8 -*-
# Робот может перемещаться в четырех направлениях («С» — север, «З» — запад, «Ю» — юг, «В» — восток)
# и принимать три цифровые команды: 0 — продолжать движение, 1 — поворот налево, −1 — поворот направо.
# Дан символ C — исходное направление робота и целое число N — посланная ему команда.
# Вывести направление робота после выполнения полученной команды.

def new_direction(c, n):
    directions = ["С", "В", "Ю", "З"]
    index = directions.index(c)
    match n:
        case 0:
            return f"Робот продолжает двигаться на {c}"
        case 1:
            return f"Робот повернул налево и теперь движется на {directions[(index - 1) % 4]}"
        case -1:
            return f"Робот повернул направо и теперь движется на {directions[(index + 1) % 4]}"
        case _:
            return "ошибка"

def main():
    first_number = str(input("Введите исходное направление (С, З, Ю, В): ")).upper()
    second_number = int(input("Введите команду (-1, 0, 1): "))
    try:
        print(new_direction(first_number, second_number))
    except ValueError:
        print("Вы ввели не корректно направление.")

if __name__ == "__main__":
    main()