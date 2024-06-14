def main(expression):
    try:
        parts = expression.split(' ')
        if len(parts) != 3:
            raise ValueError("throws Exception: Ввод должен содержать два числа и один оператор (+, -, /, *), разделенные пробелами")

        a = int(parts[0])
        operator = parts[1]
        b = int(parts[2])

        if not (1 <= a <= 10) or not (1 <= b <= 10):
            raise ValueError("throws Exception: Числа должны быть в диапазоне от 1 до 10 включительно")
        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            result = a // b
        else:
            raise ValueError("throws Exception: Некорректный оператор. Допустимые операторы: +, -, *, /")

        return str(result)

    except ValueError as ve:
        print(f"Ошибка: {ve}")

if __name__ == "__main__":
    expression = input('Введит пример: ')
    print(main(expression))