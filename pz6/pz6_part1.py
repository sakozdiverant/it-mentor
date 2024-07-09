# -*- coding: utf-8 -*-
# Создайте класс MeansOfTransport }}(для определения цвета и марки машины), принимающий 2 аргумента при инициализации
# (марка и цвет транспортного средства). В этом классе реализуйте методы {{show_color(), выводящий на печать цвет
# транспортного средства и show_brand, для получения марки транспортного средства.
# Работаем с классом из 3 пункта. Реализуйте сеттеры и геттеры для цвета и марки транспортного средства.
# Реализуйте два класса Car и Moped, которые будут наследоваться от класса MeansOfTransport.
# При инициализации они должны принимать новый аргументы(количество колес.

class MeansOfTransport:
    def __init__(self, brand, color):
        self._brand = brand
        self._color = color

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def show_color(self):
        print(f"Цвет транспортного средства: {self.color}")

    def show_brand(self):
        return self.brand

class Car(MeansOfTransport):
    def __init__(self, brand, color, wheels):
        super().__init__(brand, color)
        self.wheels = wheels

    def show_wheels(self):
        print(f"Количество колес у машины: {self.wheels}")

class Moped(MeansOfTransport):
    def __init__(self, brand, color, wheels):
        super().__init__(brand, color)
        self.wheels = wheels

    def show_wheels(self):
        print(f"Количество колес у мопеда: {self.wheels}")

car = MeansOfTransport("ВАЗ", "Красный")
car.show_color()
print(car.show_brand())

car.color = "Синий"
car.brand = "ГАЗ"

car.show_color()
print(car.show_brand())

car2 = Car("ВАЗ", "Красный", 4)
car2.show_color()
print(car2.show_brand())
car2.show_wheels()

moped = Moped("HONDA NC750", "Черный", 2)
moped.show_color()
print(moped.show_brand())
moped.show_wheels()