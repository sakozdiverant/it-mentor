import pytest
from io import StringIO



class Test_pz6_part1_MeansOfTransport():

    def test_means_of_transport(self):
        from pz6_part1 import MeansOfTransport, Car, Moped
        vehicle = MeansOfTransport("Toyota", "Red")
        assert vehicle.brand == "Toyota"
        assert vehicle.color == "Red"

        vehicle.brand = "Honda"
        vehicle.color = "Blue"
        assert vehicle.brand == "Honda"
        assert vehicle.color == "Blue"

    def test_car(self):
        from pz6_part1 import MeansOfTransport, Car, Moped
        car = Car("Lada", "White", 4)
        assert car.brand == "Lada"
        assert car.color == "White"
        assert car.wheels == 4

        car.brand = "Ford"
        car.color = "Black"
        assert car.brand == "Ford"
        assert car.color == "Black"

    def test_moped(self):
        from pz6_part1 import MeansOfTransport, Car, Moped
        moped = Moped("Yamaha", "Yellow", 2)
        assert moped.brand == "Yamaha"
        assert moped.color == "Yellow"
        assert moped.wheels == 2

        moped.brand = "Suzuki"
        moped.color = "Green"
        assert moped.brand == "Suzuki"
        assert moped.color == "Green"


class Test_pz6_part2_MeansOfTransport():
    def test_speed_and_wheels(self):
        from pz6_part2 import MeansOfTransport, Car, Moped
        travel_time = Moped.calculate_travel_time(10, 100)
        moped = Moped("Dodge Tomahawk", "Серебристый", 3)
        assert travel_time == 0.1
        assert moped.wheels == 3


class Test_pz6_part3_MeansOfTransport():
    def test_secret(self):
        from pz6_part3 import MeansOfTransport, Car, Moped
        my_car = Car("V8", "Automatic")
        assert my_car.engine == "V8"
        assert my_car._transmission == "Automatic"
        my_car.set_mileage(100)
        assert my_car.get_mileage() == 100

        my_car._transmission = "6 speed gearbox"
        assert my_car._transmission == "6 speed gearbox"


class Test_pz6_part4_MeansOfTransport():
    def test_get(self):
        from pz6_part4 import MeansOfTransport, Car, Moped
        car1 = Car("V8", "Автомат", "LADA", "Vesta", 2022)
        car2 = Car("V6", "Механика", "УАЗ", "Патриот", 2023)

        assert car1 != car2
        assert car1 < car2

        car1 + 15000
        assert len(car1) == 15000


class Test_pz6_part5_MeansOfTransport():
    def test_calculator(self):
        from pz6_part5 import Calculator, StringCalculator
        calc = Calculator()
        assert calc.add(3, 5) == 8
        calc_str = StringCalculator()
        assert calc_str.addstr('Alexandr', 'Kirichenko') == 'AlexandrKirichenko'



class Test_pz6_part6_MeansOfTransport():
    def test_inheritance(self):
        from pz6_part6 import Cat
        cat = Cat()
        assert cat.voice() == 'Meow'

class Test_pz6_part7_MeansOfTransport():
    def test_cristall(self):
        from pz6_part7 import c1
        cristall = c1('row row row your boat')
        assert cristall.tokens == ['row', 'row', 'row', 'your', 'boat']
        assert cristall.vocab == {'boat', 'your', 'row'}
        assert cristall.word_count == 5

class Test_pz6_part8_MeansOfTransport():
    def test_singelton(self):
        from pz6_part8 import Dog
        dog1 = Dog("Sharik", "Golden Retriever", 5)
        dog2 = Dog("Max", "Labrador", 3)
        assert dog1 is dog2
        assert dog1 == dog2

class Test_pz6_part9_MeansOfTransport():
    def test_group_list(self):
        from pz6_part9 import People
        people = People(["Alice", "Grum"])
        people.add_person("Ivan")
        assert "Alice" in people
        assert "Grum" in people
        assert "Ivan" in people


class Test_pz6_part10_MeansOfTransport:
    def test_group_list(self, capsys):
        from pz6_part10 import LoggedAttributes
        obj = LoggedAttributes("value1", "value2", "value3")
        obj.attr1 = "Хочу есть"
        captured1 = capsys.readouterr()
        obj.attr2 = "я голодный"
        captured2 = capsys.readouterr()
        obj.attr3 = "С кухни вкусно пахнет"
        captured3 = capsys.readouterr()
        assert "Изменение атрибута 'attr1': value1 -> Хочу есть" in captured1.out
        assert "Изменение атрибута 'attr2': value2 -> я голодный" in captured2.out
        assert "Изменение атрибута 'attr3': value3 -> С кухни вкусно пахнет" in captured3.out



