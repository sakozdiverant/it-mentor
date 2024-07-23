# test_pz3.py
import pytest
from unittest.mock import patch
import io
import importlib
main_functions = []
for i in range(1, 12):
    module_name = f'pz3_part{i}'
    module = importlib.import_module(module_name)
    main_functions.append((module_name, module.main))

def print_home(num):
    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        main_functions[num - 1][1]()  # main_part1
        output = mock_stdout.getvalue()
        return output


# Тесты для pz3_part1
def test_pz3_part1_with_numbers():
    inputs = iter(['10', '20', '30', '0'])
    expected_output = "Среднее значение: 20.0\n"
    with patch('builtins.input', lambda _: next(inputs)):
        output = print_home(1)
        assert expected_output in output

def test_pz3_part1_no_numbers():
    inputs = iter(['0'])
    expected_output = "Вы не ввели ни одного числа.\n"
    with patch('builtins.input', lambda _: next(inputs)):
        output = print_home(1)
        assert expected_output in output

def test_pz3_part1_invalid_input():
    inputs = iter(['abc', '10', '20', '0'])
    expected_output = "Среднее значение: 15.0\n"
    with patch('builtins.input', lambda _: next(inputs)):
        output = print_home(1)
        assert expected_output in output

def test_pz3_part2_output():
    expected_output = '\n'.join(map(str, range(101))) + '\n'
    output = print_home(2)
    assert output == expected_output

def test_pz3_part3_output():
    target_line1 = "2 * 6 = 12"
    target_line2 = "3 * 6 = 18"
    target_line3 = "5 * 6 = 30"
    output = print_home(3)
    assert target_line1 in output
    assert target_line2 in output
    assert target_line3 in output

def test_pz3_part4_output():
    target_line1 = "Hello"
    target_line2 = "[1, 2, 3]"
    target_line3 = "My List"
    target_line4 = "alexandr"
    output = print_home(4)
    assert target_line1 in output
    assert target_line2 in output
    assert target_line3 in output
    assert target_line4 not in output

def test_pz3_part5_output():
    target_line1 = "90"
    target_line2 = "91"
    target_line3 = "92"
    target_line4 = "93"
    output = print_home(5)
    assert target_line1 in output
    assert target_line2 not in output
    assert target_line3 not in output
    assert target_line4 in output

def test_pz3_part6_output():
    target_line1 = "5050"
    target_line2 = "5051"
    output = print_home(6)
    assert target_line1 in output
    assert target_line2 not in output

def test_pz3_part7_output():
    target_line1 = "2 * 6 = 12"
    target_line2 = "5051"
    target_line3 = "5 * 6 = 30"
    output = print_home(7)
    assert target_line1 in output
    assert target_line2 not in output
    assert target_line3 not in output

def test_pz3_part8_output():
    target_line1 = " 7,"
    target_line2 = " 8,"
    target_line3 = " 9,"
    target_line4 = " 11,"
    output = print_home(8)
    assert target_line1 in output
    assert target_line2 not in output
    assert target_line3 not in output
    assert target_line4 in output
if __name__ == "__main__":
    pytest.main()