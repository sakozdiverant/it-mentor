expression = input("В ведите пример: ")
try:
    parts = expression.split(' ')
    if len(parts) != 3:
        raise ValueError("throws Exception: Ввод должен содержать два числа и один оператор, разделенные пробелами")

    a = int(parts[0])
    operator = parts[1]
    b = int(parts[2])

    if not (0 <= a <= 10) or not (0 <= b <= 10):
        raise ValueError("throws Exception: Числа должны быть в диапазоне от 1 до 10 включительно")
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        result = a // b
    else:
        raise ValueError("throws Exception: Некорректный оператор. Допустимые операторы: +, -, *, /")

    print(result)

except ValueError as ve:
    print(f"Ошибка: {ve}")
except ZeroDivisionError as zde:
    print(f"Ошибка: {zde}")