# -*- coding: utf-8 -*-
# Написать программу для нахождения среднего арифметического списка чисел.
# Если при вводе списка чисел была допущена ошибка (например, был передан не список, а строка),
# программа должна корректно обработать эту ошибку и выдать соответствующее сообщение.
# Информация об ошибках должна быть записана в лог.

import logging

logging.basicConfig(
    filename='average.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ExceptionCheck(Exception):
    """Общая проверка"""

class ExceptionCheckList(ExceptionCheck):
    """Класс ошибки пустой список"""

    def __init__(self, *args):
        self.messege = args[0] if args else None
    def __str__(self):
        return f"Ошибка: {self.messege}"

def main():
    while True:
        try:
            input_str = input("Введите список чисел, разделенных пробелом: ")
            if not input_str.strip():
                raise ExceptionCheckList("Строка не должна быть пустой.")
            numbers = [float(num) for num in input_str.split(' ')]
            average = sum(numbers) / len(numbers)
            logging.info(f"Среднее арифметическое списка {numbers} равно {average}")
            print(f"Среднее арифметическое: {average}")
            break

        except ValueError as e:
            print(f"Ошибка: {e}.")
            print("Попробуйте еще раз.")
            logging.info(f"Ошибка: {e} \nПопробуйте еще раз с корректными значениями списка.")
        except ExceptionCheckList as e:
            print(e)
            logging.info(e)


if __name__ == "__main__":
    main()
