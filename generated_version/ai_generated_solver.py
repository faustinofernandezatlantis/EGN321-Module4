"""
AI-generated alternate implementation.
Defect: Relies on exact floating-point equality (==) instead of a tolerance range.
"""

def ai_solver(starting_val: float, target_val: float, max_iterations: int = 100):
    val = starting_val
    iterations = 0
    # DEFECT: Exact numeric equality check fails due to floating-point rounding errors
    while val != target_val and iterations < max_iterations:
        val += (target_val - val) * 0.1
        iterations += 1
    
    return val, iterations