import math

#Дана сторона квадрата a. Найти его периметр P = 4·a
def perimeter_squer(a):
    return 4 * a
print(f"Периметр квадрата: {perimeter_squer(5)}")

# Дана сторона квадрата a. Найти его площадь{{ S = a2}}
def ploshed_area(a):
    return a * a
print(f"Площадь квадрата: {ploshed_area(4)}")

# Даны стороны прямоугольника a и b. Найти его площадь S = a·b и периметр P = 2·(a + b)
def area_perimeter_rectangle(a, b):
    area = a * b
    perimeter = 2 * (a + b)
    return area, perimeter

area, perimeter = area_perimeter_rectangle(4, 5)
print(f"Площадь прямоугольника: {area}")
print(f"Периметр прямоугольника: {perimeter}")

# Дан диаметр окружности d. Найти ее длину{{ L = π·d, π = 3.14}}
def circumference_circle(d):
    pi = 3.14
    return pi * d

print(f"Длина окружности: {circumference_circle(10)}")

# Дана длина ребра куба a. Найти объем куба V = a3 и площадь его поверхности S = 6·a2
def volume_surface_area_cube(a):
    volume = a ** 3
    surface_area = 6 * (a ** 2)
    return volume, surface_area

volume, surface_area = volume_surface_area_cube(3)
print(f"Объем куба: {volume}")
print(f"Площадь поверхности куба: {surface_area}")

# Даны длины ребер a, b, c прямоугольного параллелепипеда.
# Найти его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c)
def volume_surface_area_parallelepiped(a, b, c):
    volume = a * b * c
    surface_area = 2 * (a * b + b * c + a * c)
    return volume, surface_area

volume, surface_area = volume_surface_area_parallelepiped(2, 3, 4)
print(f"Объем параллелепипеда: {volume}")
print(f"Площадь поверхности параллелепипеда: {surface_area}")

# Найти длину окружности L и площадь круга S заданного радиуса R: L = 2·π·R, S = π·R2, π=3.14
def circumference_area_circle(R):
    pi = 3.14
    circumference = 2 * pi * R
    area = pi * R * R
    return circumference, area

if __name__ == "__main__":
    circumference, area = circumference_area_circle(5)
    print(f"Длина окружности: {circumference}")
    print(f"Площадь круга: {area}")

# Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2
def arithmetic_mean(a, b):
    return (a + b) / 2

print(f"Среднее арифметическое: {arithmetic_mean(8, 12)}")
# Даны два неотрицательных числа a и b. Найти их среднее геометрическое, т. е.
# квадратный корень из их произведения: (a·b)1/2
def geometric_mean(a, b):
    return math.sqrt(a * b)

print("Среднее геометрическое:", geometric_mean(4, 16))
# Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.
def operations_squares(a, b):
    sum_squares = a**2 + b**2
    diff_squares = a**2 - b**2
    prod_squares = a**2 * b**2
    quot_squares = a**2 / b**2
    return sum_squares, diff_squares, prod_squares, quot_squares

sum_squares, diff_squares, prod_squares, quot_squares = operations_squares(3, 2)
print(f"Сумма квадратов: {sum_squares}")
print(f"Разность квадратов: {diff_squares}")
print(f"Произведение квадратов: {prod_squares}")
print(f"Частное квадратов: {quot_squares}")
