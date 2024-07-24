# -*- coding: utf-8 -*-
# Попробуйте инициализировать несколько любых переменных в классе Car и сделайте одну переменную приватной,
# одну защищенной. Попробуйте получить к ним доступ. Какой результат?
# В классе Car добавьте переменную класса car_drive = 4 и реализуйте classmethod,
# который выводит на экран переменную car_drive

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

class Car:
    car_drive = 4
    def __init__(self, engine, transmission):
        self.engine = engine
        self._transmission = transmission
        self.__mileage = 0

    def get_mileage(self):
        return self.__mileage

    def set_mileage(self, mileage):
        if mileage >= 0:
            self.__mileage = mileage

    @classmethod
    def print_car_drive(cls):
        print(f"Car drive: {cls.car_drive}")

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
    my_car = Car("V8", "Automatic")
    print(my_car.engine)
    print(my_car._transmission)

    try:
        print(my_car.__mileage)
    except AttributeError as e:
        print(e)

    print(my_car.get_mileage())

    my_car.set_mileage(100)
    print(my_car.get_mileage())

    my_car._transmission = "6 speed gearbox"
    print(my_car._transmission)

    Car.print_car_drive()

if __name__ == '__main__':
    main()
