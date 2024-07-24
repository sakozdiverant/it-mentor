import pytest
from unittest.mock import patch
import io
import importlib
import cProfile
import pstats
import allure


class TestSuite:
    main_functions = []

    @classmethod
    def setup_class(cls):
        for i in range(1, 7):
            module_name = f'pz5_part{i}'
            module = importlib.import_module(module_name)
            cls.main_functions.append((module_name, module.main))

    @staticmethod
    def print_home_and_equal(num, expected_output, inputs=None):
        input_patch = patch('builtins.input', lambda _: next(inputs)) if inputs else None

        with input_patch if input_patch else patch('builtins.input'):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                profiler = cProfile.Profile()
                profiler.enable()
                TestSuite.main_functions[num - 1][1]()
                profiler.disable()
                output = mock_stdout.getvalue()
                stats = io.StringIO()
                ps = pstats.Stats(profiler, stream=stats).sort_stats('cumulative')
                ps.print_stats()
                allure.attach(stats.getvalue(), name=f"profiling_part{num}",
                              attachment_type=allure.attachment_type.TEXT)
            assert expected_output in output

class TestPZ5Part1(TestSuite):
    def test_read(self):
        expected_output = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
        self.print_home_and_equal(1, expected_output)

class TestPZ5Part2(TestSuite):
    def test_read_file_in_different_modes(self):
        expected_output1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
        expected_output2 = "Режим 'r+':"
        expected_output3 = "Режим 'rb+':"
        self.print_home_and_equal(2, expected_output1)
        self.print_home_and_equal(2, expected_output2)
        self.print_home_and_equal(2, expected_output3)

class TestPZ5Part3(TestSuite):
    def test_write_file_in_different_modes(self):
        expected_output1 = "Запись в режиме 'w+'"
        expected_output2 = "Запись в режиме 'wb+'"
        self.print_home_and_equal(3, expected_output1)
        self.print_home_and_equal(3, expected_output2)

class TestPZ5Part4(TestSuite):
    def test_TestPZ5Part4(self):
        expected_output1 = "pz5_part1.py size 358 byte"
        expected_output2 = "pz5_part2.py size 1003 byte"
        expected_output3 = "pz5_part3.py size 2094 byte"
        expected_output4 = "pz5_part4.py size 284 byte"
        self.print_home_and_equal(4, expected_output1)
        self.print_home_and_equal(4, expected_output2)
        self.print_home_and_equal(4, expected_output3)
        self.print_home_and_equal(4, expected_output4)

class TestPZ5Part5(TestSuite):
    def test_TestPZ5Part5(self):
        expected_output1 = "4   19/01/2012  191 NaN  1  104  248   79  3  0 NaN"
        expected_output2 = "13  28/01/2012   80 NaN  1   61  123   33  9  1 NaN"
        expected_output3 = "18  02/02/2012  217 NaN  5  134  345  128  2  2 NaN"
        expected_output4 = "Int64Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype='int64')"
        self.print_home_and_equal(5, expected_output1)
        self.print_home_and_equal(5, expected_output2)
        self.print_home_and_equal(5, expected_output3)
        self.print_home_and_equal(5, expected_output4)

class TestPZ5Part6(TestSuite):
    def test_TestPZ5Part6(self):
        expected_output1 = "5443     1"
        expected_output2 = "5168     1"
        expected_output3 = "2430     1"
        expected_output4 = "Name: Rachel1, dtype: int64"
        self.print_home_and_equal(6, expected_output1)
        self.print_home_and_equal(6, expected_output2)
        self.print_home_and_equal(6, expected_output3)
        self.print_home_and_equal(6, expected_output4)


if __name__ == "__main__":
    pytest.main(["--alluredir", "allure-results"])