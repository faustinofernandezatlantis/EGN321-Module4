"""
Deterministic engineering calculation module for ENG 321.
"""
import math


def calculate_volume(radius: float, height: float) -> float:
    """
    Calculates the volume of a cylindrical tank.
    V = pi * r^2 * h
    """
    return math.pi * (radius ** 2) * height


def calculate_target_difference(current_val: float, target_val: float) -> float:
    """
    Returns the absolute difference from the target value.
    """
    return abs(current_val - target_val)