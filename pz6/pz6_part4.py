# -*- coding: utf-8 -*-
# Реализуйте все возможные магические методы в классе Car.
# __str__ и __repr__: для строкового и официального представления объекта.
# __eq__ и __lt__: для сравнения объектов.
# __add__: для добавления пробега к машине.
# __len__: для получения текущего пробега.
# __getattr__, __setattr__, и __delattr__: для доступа, установки и удаления атрибутов.
# __enter__ и __exit__: для поддержки менеджеров контекста.

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

    def __init__(self, engine, transmission, make, model, year, mileage=0):
        self.engine = engine
        self._transmission = transmission
        self.__mileage = mileage
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model} with {self.engine} engine and {self._transmission} transmission"

    def __repr__(self):
        return (f"Car(engine={self.engine}, transmission={self._transmission}, make={self.make}, "
                f"model={self.model}, year={self.year}, mileage={self.__mileage})")

    def __eq__(self, other):
        if isinstance(other, Car):
            return (self.make == other.make and
                    self.model == other.model and
                    self.year == other.year and
                    self.engine == other.engine and
                    self._transmission == other._transmission)
        return False

    def __lt__(self, other):
        if isinstance(other, Car):
            return self.year < other.year
        return NotImplemented

    def __add__(self, miles):
        if isinstance(miles, (int, float)):
            self.__mileage += miles
            return self
        return NotImplemented

    def __len__(self):
        return self.__mileage

    def __getattr__(self, name):
        return f"'Car' object has no attribute '{name}'"

    def __setattr__(self, name, value):
        if name == "mileage":
            if value >= 0:
                self.__dict__["_Car__mileage"] = value
            else:
                raise ValueError("Mileage cannot be negative")
        else:
            super().__setattr__(name, value)

    # Deleting attributes
    def __delattr__(self, name):
        if name == "mileage":
            raise AttributeError("Cannot delete mileage attribute")
        else:
            super().__delattr__(name)

    @classmethod
    def print_car_drive(cls):
        print(f"Car drive: {cls.car_drive}")

    def __enter__(self):
        print(f"Entering the context of {self}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Exiting the context of {self}")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return True  # Suppress exceptions

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
    car1 = Car("V8", "Автомат", "LADA", "Vesta", 2022)
    car2 = Car("V6", "Механика", "УАЗ", "Патриот", 2023)

    print(car1)
    print(repr(car1))

    print(car1 == car2)
    print(car1 < car2)   # Вывод: True (так как 2022 > 2023)

    car1 + 15000  # Добавляет пробег
    print(len(car1))  # Вывод: 15000

    with car1 as c:
        print("Inside the context")

if __name__ == '__main__':
    main()

