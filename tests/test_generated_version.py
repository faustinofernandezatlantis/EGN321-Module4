from generated_version.ai_generated_solver import ai_solver


def test_exposes_ai_generated_version_defect():
    """
    Exposes defect in AI solver which uses exact floating-point equality (==).
    Due to precision limits, starting at 1.0 trying to hit 10.0 will hit max iterations
    without reaching exact equality.
    """
    final_val, iterations = ai_solver(starting_val=1.0, target_val=10.0, max_iterations=50)
    # The solver terminates due to max_iterations rather than achieving exact equality
    assert final_val != 10.0
    assert iterations == 50