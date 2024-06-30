# Посчитать сумму квадратов чисел от 1 до 10.
def main():
    result = sum(i ** 2 for i in range(1, 11))
    print(f"Сумма квадратов чисел от 1 до 10: {result}")

if __name__ == "__main__":
    main()
