import math
from src.calculation import calculate_volume, calculate_target_difference


def test_calculate_volume_correctness():
    # V = pi * (2^2) * 5 = 20 * pi
    result = calculate_volume(2.0, 5.0)
    assert abs(result - (math.pi * 4 * 5)) < 1e-5


def test_calculate_target_difference():
    diff = calculate_target_difference(10.5, 10.0)
    assert abs(diff - 0.5) < 1e-5