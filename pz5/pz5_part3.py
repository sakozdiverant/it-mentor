# -*- coding: utf-8 -*-
# Попробуйте открыть файлы с разными значениями mode для чтения.

def write_file_in_different_modes(filename):
    # Режим записи текста
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Запись в режиме 'w'. Это перезаписывает содержимое файла.\n")

    # Режим записи байтов
    with open(filename, 'wb') as file:
        file.write("Запись в режиме 'wb'. Это перезаписывает содержимое файла.\n".encode('utf-8'))

    # Режим добавления текста
    with open(filename, 'a', encoding='utf-8') as file:
        file.write("Запись в режиме 'a'. Это добавляется в конец файла.\n")

    # Режим добавления байтов
    with open(filename, 'ab') as file:
        file.write("Запись в режиме 'ab'. Это добавляется в конец файла.\n".encode('utf-8'))

    # Режим чтения и записи текста
    with open(filename, 'w+', encoding='utf-8') as file:
        file.write("Запись в режиме 'w+'. Это перезаписывает содержимое файла и позволяет читать.\n")
        file.seek(0)
        print("Содержимое файла после записи в режиме 'w+':")
        print(file.read())

    # Режим чтения и записи байтов
    with open(filename, 'wb+') as file:
        file.write("Запись в режиме 'wb+'. Это перезаписывает содержимое файла и позволяет читать.\n".encode('utf-8'))
        file.seek(0)
        print("Содержимое файла после записи в режиме 'wb+':")
        print(file.read().decode('utf-8'))

def main():
    write_file_in_different_modes('write_lorum.txt')


if __name__ == '__main__':
    main()


