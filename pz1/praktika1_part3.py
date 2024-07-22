# Дано целое число A. Проверить истинность высказывания: «Число A является положительным».
def is_positive(a):
    return a > 0
if __name__ == "__main__":
    print(is_positive(5))

# Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».
def is_odd(a):
    return a % 2 != 0
if __name__ == "__main__":
    print(is_odd(5))

# Дано целое число A. Проверить истинность высказывания: «Число A является четным».
def is_even(a):
    return a % 2 == 0
if __name__ == "__main__":
    print(is_even(4))

# Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A > 2 и B ≤ 3».
def check_inequalities_1(A, B):
    return A > 2 and B <= 3
if __name__ == "__main__":
    print(check_inequalities_1(3, 3))

# Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A ≥ 0 или B < −2».
def check_inequalities_2(A, B):
    return A >= 0 or B < -2
if __name__ == "__main__":
    print(check_inequalities_2(-1, -3))

# Даны три целых числа: A, B, C. Проверить истинность высказывания: «Справедливо двойное неравенство A < B < _C_».
def check_double_inequality(A, B, C):
    return A < B < C
if __name__ == "__main__":
    print(check_double_inequality(1, 2, 3))

# Даны три целых числа: A, B, C. Проверить истинность высказывания: «Число B находится между числами A и _C_».
def is_between(A, B, C):
    return A < B < C or C < B < A
if __name__ == "__main__":
    print(is_between(1, 2, 3))

# Даны два целых числа: A, B. Проверить истинность высказывания: «Каждое из чисел A и B нечетное».
def both_odd(A, B):
    return A % 2 != 0 and B % 2 != 0
if __name__ == "__main__":
    print(both_odd(3, 5))

# Даны два целых числа: A, B. Проверить истинность высказывания: «Хотя бы одно из чисел A и B нечетное».
def least(A, B):
    return A % 2 != 0 or B % 2 != 0
if __name__ == "__main__":
    print(least(2, 3))

# Даны два целых числа: A, B. Проверить истинность высказывания: «Ровно одно из чисел A и B нечетное»
def exactly(A, B):
    return (A % 2 != 0) != (B % 2 != 0)
if __name__ == "__main__":
    print(exactly(2, 3))
