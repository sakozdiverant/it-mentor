# -*- coding: utf-8 -*-
# Робот может перемещаться в четырех направлениях («С» — север, «З» — запад, «Ю» — юг, «В» — восток)
# и принимать три цифровые команды: 0 — продолжать движение, 1 — поворот налево, −1 — поворот направо.
# Дан символ C — исходное направление робота и целое число N — посланная ему команда.
# Вывести направление робота после выполнения полученной команды.
def main():
    first_number = str(input("Введите исходное направление (С, З, Ю, В): ")).upper()
    second_number = int(input("Введите команду (-1, 0, 1): "))
    # third_number = int(input("Введите третье число: "))

    directions = ['С', 'В', 'Ю', 'З']
    current_index = directions.index(first_number)

    if second_number == 0:
        print(f"Робот продолжает двигаться на {first_number}")
    elif second_number == 1:
        new_direction = directions[(current_index - 1) % 4]
        print(f"Робот повернул налево и теперь движется на {new_direction}")
    elif second_number == -1:
        new_direction = directions[(current_index + 1) % 4]
        print(f"Робот повернул направо и теперь движется на {new_direction}")
    else:
        print("ошибка")

if __name__ == "__main__":
    main()