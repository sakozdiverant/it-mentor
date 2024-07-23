import pytest
from unittest.mock import patch
import io
import importlib
import cProfile
import pstats
import allure
from pz4_part10 import number_to_words, calculator

class TestSuite:
    main_functions = []

    @classmethod
    def setup_class(cls):
        for i in range(1, 11):
            module_name = f'pz4_part{i}'
            module = importlib.import_module(module_name)
            cls.main_functions.append((module_name, module.main))

    @staticmethod
    def print_home_and_equal(num, expected_output, inputs):
        with patch('builtins.input', lambda _: next(inputs)):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                profiler = cProfile.Profile()
                profiler.enable()
                TestSuite.main_functions[num - 1][1]()
                profiler.disable()
                output = mock_stdout.getvalue()
                stats = io.StringIO()
                ps = pstats.Stats(profiler, stream=stats).sort_stats('cumulative')
                ps.print_stats()
                allure.attach(stats.getvalue(), name=f"profiling_part{num}", attachment_type=allure.attachment_type.TEXT)
            assert expected_output in output

class TestPZ4Part1(TestSuite):
    def test_3plus(self):
        inputs = iter(['5', '10', '7'])
        expected_output = "Количество положительных чисел: 3"
        self.print_home_and_equal(1, expected_output, inputs)

    def test_0(self):
        inputs = iter(['-5', '0', '-1'])
        expected_output = "Количество положительных чисел: 0"
        self.print_home_and_equal(1, expected_output, inputs)

class TestPZ4Part2(TestSuite):
    def test_positive_numbers(self):
        inputs = iter(['5', '2'])
        expected_output = "Большее число: 5"
        self.print_home_and_equal(2, expected_output, inputs)

    def test_negative_numbers(self):
        inputs = iter(['-5', '2'])
        expected_output = "Большее число: 2"
        self.print_home_and_equal(2, expected_output, inputs)

class TestPZ4Part3(TestSuite):
    def test_pz4_part3(self):
        inputs = iter(['5', '2'])
        expected_output = "Большее: 5, Меньшее: 2"
        self.print_home_and_equal(3, expected_output, inputs)

    def test_pz4_part3_minus(self):
        inputs = iter(['-5', '2'])
        expected_output = "Большее: 2, Меньшее: -5"
        self.print_home_and_equal(3, expected_output, inputs)

class TestPZ4Part4(TestSuite):
    def test_pz4_part4(self):
        inputs = iter(['5', '2', '1'])
        expected_output = "Наименьшее число: 1"
        self.print_home_and_equal(4, expected_output, inputs)

    def test_pz4_part4_minus(self):
        inputs = iter(['-5', '0', '-1'])
        expected_output = "Наименьшее число: -5"
        self.print_home_and_equal(4, expected_output, inputs)

class TestPZ4Part5(TestSuite):
    def test_pz4_part5(self):
        for x in range(-2, 3):
            for y in range(-2, 3):
                inputs = iter([x, y])
                if x > 0 and y > 0:
                    expected_output = "Точка находится в первой четверти"
                elif x < 0 and y > 0:
                    expected_output = "Точка находится во второй четверти"
                elif x < 0 and y < 0:
                    expected_output = "Точка находится в третьей четверти"
                elif x > 0 and y < 0:
                    expected_output = "Точка находится в четвертой четверти"
                else:
                    expected_output = ""
                self.print_home_and_equal(5, expected_output, inputs)

class TestPZ4Part6(TestSuite):
    def test_pz4_part6(self):
        def grade(k):
            match k:
                case 1:
                    return "плохо"
                case 2:
                    return "неудовлетворительно"
                case 3:
                    return "удовлетворительно"
                case 4:
                    return "хорошо"
                case 5:
                    return "отлично"
                case _:
                    return "ошибка"
        for i in range(0, 6):
            inputs = iter([i])
            self.print_home_and_equal(6, grade(i), inputs)

class TestPZ4Part7(TestSuite):
    def test_pz4_part7_february(self):
        inputs = iter(['2'])
        expected_output = "28"
        self.print_home_and_equal(7, expected_output, inputs)

    def test_pz4_part7_may(self):
        inputs = iter(['5'])
        expected_output = "31"
        self.print_home_and_equal(7, expected_output, inputs)

class TestPZ4Part8(TestSuite):
    def test_pz4_part8_february(self):
        inputs = iter(['2', '28'])
        expected_output = "Следующая дата: День 1 месяц 3"
        self.print_home_and_equal(8, expected_output, inputs)

    def test_pz4_part8_may(self):
        inputs = iter(['5', '12'])
        expected_output = "Следующая дата: День 13 месяц 5"
        self.print_home_and_equal(8, expected_output, inputs)

class TestPZ4Part10:
    @pytest.mark.parametrize("num, expected", [
        (100, "сто"),
        (256, "двести пятьдесят шесть"),
        (814, "восемьсот четырнадцать"),
        (999, "девятьсот девяносто девять"),
        (101, "сто один"),
        (112, "сто двенадцать"),
        (120, "сто двадцать"),
        (133, "сто тридцать три")
    ])
    def test_number_to_words(self, num, expected):
        assert number_to_words(num) == expected

    def test_number_to_words_out_of_range(self):
        assert number_to_words(99) == "Число должно быть в диапазоне от 100 до 999"
        assert number_to_words(1000) == "Число должно быть в диапазоне от 100 до 999"

    @pytest.mark.parametrize("inputs, expected_output", [
        (["10", "5", "+"], "Результат: 15.0"),
        (["10", "5", "-"], "Результат: 5.0"),
        (["10", "5", "*"], "Результат: 50.0"),
        (["10", "5", "/"], "Результат: 2.0"),
        (["10", "0", "/"], "Ошибка: деление на ноль"),
        (["10", "5", "^"], "Ошибка: недопустимая операция"),
        (["abc", "5", "+"], "Ошибка: введите допустимые числа"),
        (["10", "abc", "+"], "Ошибка: введите допустимые числа")
    ])
    def test_calculator(self, inputs, expected_output):
        with patch('builtins.input', side_effect=inputs):
            assert calculator() == expected_output


if __name__ == "__main__":
    pytest.main(["--alluredir", "allure-results"])