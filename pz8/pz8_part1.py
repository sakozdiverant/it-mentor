# -*- coding: utf-8 -*-
# Дано число в диапазоне от 1_000_000 до 20_000_000. Получите список целочисленных делителей этого числа.
# Напишите скрипт который создаст параллельно 10 файлов с именем `file_ {index}.txt'
# и записывает их номер внутрь файла.

import concurrent.futures
import os

def find_divisors(n): #task1
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def create_file(index): #task2
    filename = f'file_{index}.txt'
    with open(filename, 'w') as f:
        f.write(str(index))
    #print(f'Created {filename}')

#Для параллельного создания файлов concurrent.futures.ThreadPoolExecutor
def main():
    number = 10050000

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(find_divisors, number)
        divisors = future.result()
    print(f'Divisors of {number}: {divisors}')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(create_file, range(1, 11)) #map: выполнения множества однотипных задач

if __name__ == "__main__":
    main()
