# Используя операции индексирования и среза выведите на экран первый и третий
# элементы списка [1, 2, 3 ,4 ,5], а также срез списка из первых трех элементов.
lst = [1, 2, 3, 4, 5]
first_element = lst[0]
third_element = lst[2]
first_three_elements = lst[:3]
print(f"Первый элемент:", first_element)
print(f"Третий элемент:", third_element)
print(f"Срез первых трех элементов:", first_three_elements)
print("------------------------------")

# Дан список [«Ростов», «+», «на», «-», «Дону»]. Исправьте плюс на дефис и выведите название
# города на экран использовав доступ к элементам списка по индексам
city = ["Ростов", "+", "на", "-", "Дону"]
city[1] = "-"
print(f"Название города: {city[0]} {city[1]} {city[2]} {city[3]} {city[4]}")
print("------------------------------")
# Дан список [«a», «s», «1», «a», «32», «23»]. Разбейте его на два списка: только с
# буквами и только с числами.
mixed_list = ["a", "s", "1", "a", "32", "23"]
letters = []
numbers = []
for item in mixed_list:
    if item.isdigit():
        numbers.append(item)
    elif item.isalpha():
        letters.append(item)

print(f"Список с буквами: {letters}")
print(f"Список с числами: {numbers}")
print("------------------------------")

# В предыдущей задаче должен был получиться список из букв. Используя методы списков:
# удалите из него последний элемент, сделайте реверсию списка.
letters.pop()
letters.reverse()

print(f"Модифицированный список с буквами: {letters}")
print("------------------------------")

# Преобразуйте список [«a», «s», «1», «a», «32», «23»] в set и выведите на экран. Что изменилось?
original_list = ["a", "s", "1", "a", "32", "23"]
unique_set = set(original_list)

print(f"Множество: {unique_set}")
