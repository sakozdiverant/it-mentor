# -*- coding: utf-8 -*-
# Напишите программу для подсчета среднего числа всех введенных пользователям чисел.
# Ввод пользователя должен осуществляться с помощью input. Если пользователь вводит ноль,
# то выводиться на экран среднее значение. Используйте цикл while для решения данной задачи

import logging

# Настройка логгирования
logging.basicConfig(
    filename='average_calculator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    total_sum = 0
    count = 0

    while True:
        try:
            number = float(input("Введите число (0 для завершения): "))

            if number == 0:
                if count == 0:
                    print("Вы не ввели ни одного числа.")
                    logging.info("Попытка вычисления среднего без ввода чисел.")
                else:
                    average = total_sum / count
                    print(f"Среднее значение: {average}")
                    logging.info(f"Среднее значение {average} рассчитано из {count} чисел с общей суммой {total_sum}.")
                break

            total_sum += number
            count += 1

        except ValueError as e:
            print("Ошибка: Введите действительное число.")
            logging.error(f"Ошибка ввода: {e}")


if __name__ == "__main__":
    main()
