# Написать программу на Python для решения квадратного уравнения ax^2 + bx + c = 0.
# Если дискриминант отрицателен, программа должна выдать ошибку и предложить пользователю
# попробовать еще раз с другими коэффициентами. При выполнении скрипта в лог должна записываться
# информация о успехе или неудаче операции.

import logging
import math

logging.basicConfig(
    filename='quadratic_solver.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def solve_quadratic(a, b, c):
    try:
        d = b ** 2 - 4 * a * c

        if d < 0:
            raise ValueError(f"Дискриминант отрицателен, уравнение не имеет вещественных корней. "
                             f"\n Дискриминант D = {d}")

        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)

        logging.info(f'Корни уравнения: x1={x1}, x2={x2}, Дискриминант D = {d}')
        return x1, x2, d

    except ValueError as e:
        logging.error(e)
        raise

def main():
    while True:
        try:
            a = float(input("Введите коэффициент a: "))
            b = float(input("Введите коэффициент b: "))
            c = float(input("Введите коэффициент c: "))

            x1, x2, d = solve_quadratic(a, b, c)
            print(f'Корни уравнения: x1 = {x1}, x2 = {x2}, Дискриминант D = {d}')
            break

        except ValueError as e:
            print(f"Ошибка: {e}")
            print("Попробуйте еще раз с другими коэффициентами.")
            logging.info("Попробуйте еще раз с другими коэффициентами.")


if __name__ == "__main__":
    main()
