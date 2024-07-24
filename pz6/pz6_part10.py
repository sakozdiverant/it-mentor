# -*- coding: utf-8 -*-
# Напишите класс, содержит 3 любые атрибута и при изменении логгировать всё в
# консоль (при изменении старое->новое)

class LoggedAttributes:
    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3

    def __setattr__(self, name, value):
        if name in self.__dict__:
            old_value = self.__dict__[name]
            print(f"Изменение атрибута '{name}': {old_value} -> {value}")
        else:
            print(f"Установка атрибута '{name}' со значением {value}")
        super().__setattr__(name, value)



def main():
    obj = LoggedAttributes("value1", "value2", "value3")
    obj.attr1 = "Хочу есть"
    obj.attr2 = "я голодный"
    obj.attr3 = "С кухни вкусно пахнет"

    obj.new_attr = "new_value"
    obj.new_attr = "Наконец пора перходить к Теории"

if __name__ == '__main__':
    main()