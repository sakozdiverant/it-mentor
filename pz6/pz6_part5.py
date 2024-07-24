# -*- coding: utf-8 -*-
# Реализуйте класс Calculator, в котором будет один метод, для вычисления суммы двух чисел.
# Реализуйте еще один класс, который будет наследоваться от класса Calculator и перегрузите метод
# для вычисления суммы двух чисел, чтобы он делал конкатенацию двух строк.

class Calculator:
    def add(self, a, b):
        result = a + b
        return result

class StringCalculator(Calculator):
    def addstr(self, a, b):
        if isinstance(a, str) and isinstance(b, str):
            return self.add(a, b)
        else:
            raise TypeError("Оба аргумента должны быть строками для конкатенации")


def main():
    calc = Calculator()
    print(calc.add(3, 5))

    str_calc = StringCalculator()
    print(str_calc.addstr("Hello, ", "world!"))

    try:
        print(str_calc.addstr(3, 5))
    except TypeError as e:
        print(e)

if __name__ == '__main__':
    main()