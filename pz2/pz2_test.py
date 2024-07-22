import unittest
from unittest.mock import patch
from io import StringIO

from praktika2_part1 import solve_quadratic
from praktika2_part2 import generate_random_number
from praktika2_part3 import main

class TestQuadraticSolver(unittest.TestCase):

    def test_two_real_roots(self):
        a, b, c = 1, -5, 6
        x1, x2, d = solve_quadratic(a, b, c)
        self.assertAlmostEqual(x1, 3)
        self.assertAlmostEqual(x2, 2)
        self.assertAlmostEqual(d, 1)

    def test_one_real_root(self):
        a, b, c = 1, -4, 4
        x1, x2, d = solve_quadratic(a, b, c)
        self.assertAlmostEqual(x1, 2)
        self.assertAlmostEqual(x2, 2)
        self.assertAlmostEqual(d, 0)

    def test_no_real_roots(self):
        a, b, c = 1, 1, 1
        with self.assertRaises(ValueError):
            solve_quadratic(a, b, c)

class TestRandomNumberGenerator(unittest.TestCase):

    def test_valid_range(self):
        min_val, max_val = 1, 10
        result = generate_random_number(min_val, max_val)
        self.assertIn(result, range(min_val, max_val + 1))

    def test_negative_min_value(self):
        with self.assertRaises(ValueError) as context:
            generate_random_number(-1, 10)
        self.assertEqual(str(context.exception), "Границы диапазона должны быть неотрицательными")

    def test_negative_max_value(self):
        with self.assertRaises(ValueError) as context:
            generate_random_number(1, -10)
        self.assertEqual(str(context.exception), "Границы диапазона должны быть неотрицательными")

    def test_min_greater_than_max(self):
        with self.assertRaises(ValueError) as context:
            generate_random_number(10, 1)
        self.assertEqual(str(context.exception), "Минимальное значение не может быть больше "
                                                 "максимального значения.")

class TestAverageCalculation(unittest.TestCase):

    def setUp(self):
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    @patch('builtins.input', side_effect=['1 2 3 4 5'])
    def test_valid_input(self, mock_input):
        main()
        output = self.mock_stdout.getvalue().strip()
        self.assertIn("Среднее арифметическое: 3.0", output)

    @patch('builtins.input', side_effect=['10 20 30'])
    def test_different_numbers(self, mock_input):
        main()
        output = self.mock_stdout.getvalue().strip()
        self.assertIn("Среднее арифметическое: 20.0", output)



if __name__ == '__main__':
    unittest.main()

# для запуска необходима находиться в каталоге с тестом python -m unittest pz2_test.py