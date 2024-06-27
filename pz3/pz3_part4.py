# -*- coding: utf-8 -*-
# Создайте список с разными значениями, пройдитесь по нему в цикле и выведите на экран.
# (Сделайте тоже самое со словарем и выведите ключ и значение)


list_value = [1, "Hello", 3.14, True, None, [1, 2, 3]]
print('My List')
for item in list_value:
    print(item)

print('\nMy Dict')
list_key = ['int', 'str', 'float', 'Boolean', 'None', 'List']
my_dict = dict(zip(list_key, list_value))
for key, value in my_dict.items():
    print(f"{key}: {value}")