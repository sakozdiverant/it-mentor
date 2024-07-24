# -*- coding: utf-8 -*-
# В классе Moped напишите статическую функцию, которая на вход будет принимать расстояние и
# максимальную скорость, а на выходе получать время, за которое проедет мопед это расстояние.

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

    @staticmethod
    def calculate_travel_time(distance, max_speed):
        return distance / max_speed

def main():
    travel_time = Moped.calculate_travel_time(100, 613)
    moped = Moped("Dodge Tomahawk", "Серебристый", 2)
    moped.show_color()
    print(moped.show_brand())
    moped.show_wheels()
    print(f"Время, необходимое для проезда 100 км при максимальной скорости 613 км/ч: {travel_time * 60} минут")

if __name__ == '__main__':
    main()
