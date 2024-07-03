# -*- coding: utf-8 -*-
# Попробуйте открыть файлы с разными значениями mode для чтения.

def read_file_in_different_modes(filename):

    with open(filename, 'r', encoding='utf-8') as file:
        print("Режим 'r':")
        print(file.read())

    print('----------------------------------------------')
    with open(filename, 'rb') as file:
        print("Режим 'rb':")
        print(file.read())

    print('----------------------------------------------')
    with open(filename, 'r+', encoding='utf-8') as file:
        print("Режим 'r+':")
        content = file.read()
        print(content)


    print('----------------------------------------------')
    with open(filename, 'rb+') as file:
        print("Режим 'rb+':")
        content = file.read()
        print(content)
        print()

read_file_in_different_modes('lorum.txt')
