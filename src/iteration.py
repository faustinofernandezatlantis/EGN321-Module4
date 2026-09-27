"""
Iterative solver module handling state management and history tracking.
"""
import math
from typing import Dict, Any, List
from src.validation import validate_inputs
from src.calculation import calculate_volume


class CalculationStatus:
    CONVERGED = "CONVERGED"
    NOT_CONVERGED = "NOT CONVERGED"
    INVALID_INPUT = "INVALID INPUT"


def run_iterative_solver(
    initial_value: float,
    target_value: float,
    height: float,
    tolerance: float = 1e-3,
    max_iterations: int = 50
) -> Dict[str, Any]:
    """
    Iteratively adjusts radius to size a tank for a target volume.
    """
    # 1. Input Validation
    is_valid, error_msg = validate_inputs(
        initial_value, target_value, height, tolerance, max_iterations
    )
    if not is_valid:
        return {
            "status": CalculationStatus.INVALID_INPUT,
            "final_value": None,
            "final_error": None,
            "iterations_performed": 0,
            "history": [],
            "error_message": error_msg
        }

    current_val = initial_value
    history: List[Dict[str, Any]] = []
    status = CalculationStatus.NOT_CONVERGED

    for iteration in range(1, max_iterations + 1):
        current_result = calculate_volume(current_val, height)
        diff = current_result - target_value
        abs_error = abs(diff)

        history.append({
            "iteration": iteration,
            "evaluated_value": current_val,
            "produced_result": current_result,
            "target": target_value,
            "error": abs_error
        })

        # Check convergence condition
        if abs_error <= tolerance:
            status = CalculationStatus.CONVERGED
            break

        # Proportional adjustment step
        derivative = 2 * math.pi * current_val * height
        adjustment = diff / derivative if derivative != 0 else 0.01
        current_val -= adjustment

        # Prevent non-physical negative or zero dimensions
        if current_val <= 0:
            current_val = 1e-4

    return {
        "status": status,
        "final_value": current_val,
        "final_error": history[-1]["error"] if history else None,
        "iterations_performed": len(history),
        "history": history,
        "error_message": None
    }