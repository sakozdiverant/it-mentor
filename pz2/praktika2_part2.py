# -*- coding: utf-8 -*-
# Написать программу для генерации случайных чисел в заданном диапазоне.
# Если пользователь ввел недопустимые границы диапазона (например, меньше нуля),
# программа должна вывести ошибку и попросить ввести диапазон заново. Информация об ошибках
# должна быть записана в лог.

import random
import logging

logging.basicConfig(
    filename='random.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def generate_random_number(min_val, max_val):
    try:
        if min_val < 0 or max_val < 0:
            raise ValueError("Границы диапазона должны быть неотрицательными")
        if min_val > max_val:
            raise ValueError("Минимальное значение не может быть больше максимального значения.")

        random_number = random.randint(min_val, max_val)
        logging.info(f"Сгенерировано случайное число: {random_number} в диапазоне ({min_val}, {max_val})")
        return random_number

    except ValueError as e:
        logging.error(e)
        raise

def main():
    while True:
        try:
            min_val = int(input("Введите минимальное значение диапазона: "))
            max_val = int(input("Введите максимальное значение диапазона: "))

            random_number = generate_random_number(min_val, max_val)
            print(f"Случайное число: {random_number}")
            break

        except ValueError as e:
            print(f"Ошибка: {e}")
            print("Попробуйте еще раз с другими значениями диапазона.")
            logging.info("Попробуйте еще раз с другими значениями диапазона.")

if __name__ == "__main__":
    main()
