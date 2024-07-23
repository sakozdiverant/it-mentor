# -*- coding: utf-8 -*-
#Откройте и прочитайте данные с файла lorum.txt,
# способом, который рассматривается в видео из пункта 1.
def main():
    file = open('lorum.txt', 'r', encoding='utf-8')
    print(file.read())
    file.close()

if __name__ == '__main__':
    main()
