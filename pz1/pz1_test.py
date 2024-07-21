import pytest
from praktika1_part1 import (
    perimeter_squer,
    ploshed_area,
    area_perimeter_rectangle,
    circumference_circle,
    volume_surface_area_cube,
    volume_surface_area_parallelepiped,
    circumference_area_circle,
    arithmetic_mean,
    geometric_mean,
    operations_squares
)

def test_perimeter_squer():
    assert perimeter_squer(4) == 16

def test_area():
    assert ploshed_area(4) == 16

def test_area_perimeter_rectangle():
    area, perimeter = area_perimeter_rectangle(4, 5)
    assert area == 20
    assert perimeter == 18

def test_circumference_circle():
    assert circumference_circle(4) == pytest.approx(12.566, 0.001)

def test_volume_surface_area_cube():
    volume, surface_area = volume_surface_area_cube(3)
    assert volume == 27
    assert surface_area == 54

def test_volume_surface_area_parallelepiped():
    volume, surface_area = volume_surface_area_parallelepiped(2, 3, 4)
    assert volume == 24
    assert surface_area == 52

def test_circumference_area_circle():
    circumference, area = circumference_area_circle(5)
    assert circumference == pytest.approx(31.415, 0.001)
    assert area == pytest.approx(78.54, 0.01)

def test_arithmetic_mean():
    assert arithmetic_mean(3, 5) == 4

def test_geometric_mean():
    assert geometric_mean(3, 5) == pytest.approx(3.872, 0.001)

def test_operations_squares():
    sum_squares, diff_squares, prod_squares, quot_squares = operations_squares(3, 2)
    assert sum_squares == 13
    assert diff_squares == 5
    assert prod_squares == 36
    assert quot_squares == 2.25

from praktika1_part2 import (
    full_meters,
    full_tons,
    full_kilobytes,
    segments_count,
    remaining_length,
    digits_number,
    sum_product_digits,
    swap_digits,
    first_digit_of_three_digit_number,
    last_and_middle_digits
)

def test_arithmetic_mean():
    assert full_meters(5) == 0

def test_full_tons():
    assert full_tons(5) == 0

def test_full_kilobytes():
    assert full_kilobytes(5000) == 4

def test_segments_count():
    assert segments_count(5000, 1024) == 4

def test_remaining_length():
    assert remaining_length(7, 6) == 1

def test_digits_number():
    assert digits_number(78) == (7, 8)

def test_sum_product_digits():
    assert sum_product_digits(78) == (15, 56)

def test_swap_digits():
    assert swap_digits(78) == 87

def test_first_digit_of_three_digit_number():
    assert first_digit_of_three_digit_number(587) == 5

def test_last_and_middle_digits():
    assert last_and_middle_digits(587) == (7, 8)