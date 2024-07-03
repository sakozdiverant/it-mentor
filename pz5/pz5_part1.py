# -*- coding: utf-8 -*-
#Откройте и прочитайте данные с файла lorum.txt,
# способом, который рассматривается в видео из пункта 1.

file = open('lorum.txt', 'r', encoding='utf-8')
print(file.read())
file.close()
