"""
Input validation module for engineering requirements.
"""
from typing import Tuple


def validate_inputs(
    initial_value: float,
    target_value: float,
    height: float,
    tolerance: float,
    max_iterations: int
) -> Tuple[bool, str]:
    """
    Validates solver inputs before execution.
    Returns (is_valid, error_message).
    """
    if initial_value <= 0:
        return False, "Initial value (radius) must be a positive number greater than zero."
    if target_value <= 0:
        return False, "Target volume must be greater than zero."
    if height <= 0:
        return False, "Tank height must be greater than zero."
    if tolerance <= 0:
        return False, "Convergence tolerance must be greater than zero."
    if max_iterations < 1 or not isinstance(max_iterations, int):
        return False, "Maximum iterations must be a positive integer (at least 1)."
    
    return True, ""