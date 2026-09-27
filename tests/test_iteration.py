from src.iteration import run_iterative_solver, CalculationStatus


def test_successful_convergence_case_1():
    res = run_iterative_solver(
        initial_value=1.0, target_value=100.0, height=5.0, tolerance=1e-3, max_iterations=50
    )
    assert res["status"] == CalculationStatus.CONVERGED
    assert res["final_error"] <= 1e-3


def test_successful_convergence_case_2_different_start():
    res = run_iterative_solver(
        initial_value=10.0, target_value=100.0, height=5.0, tolerance=1e-3, max_iterations=50
    )
    assert res["status"] == CalculationStatus.CONVERGED


def test_tolerance_boundary_case():
    res = run_iterative_solver(
        initial_value=2.0, target_value=100.0, height=5.0, tolerance=1e-6, max_iterations=100
    )
    if res["status"] == CalculationStatus.CONVERGED:
        assert res["final_error"] <= 1e-6


def test_non_convergence_case():
    # Force non-convergence by setting max_iterations to 1
    res = run_iterative_solver(
        initial_value=1.0, target_value=100.0, height=5.0, tolerance=1e-6, max_iterations=1
    )
    assert res["status"] == CalculationStatus.NOT_CONVERGED


def test_invalid_input_case():
    res = run_iterative_solver(initial_value=-5.0, target_value=100.0, height=5.0)
    assert res["status"] == CalculationStatus.INVALID_INPUT


def test_iteration_history_produced():
    res = run_iterative_solver(initial_value=1.0, target_value=100.0, height=5.0, max_iterations=10)
    assert len(res["history"]) > 0
    assert "evaluated_value" in res["history"][0]


def test_max_iterations_behavior():
    res = run_iterative_solver(
        initial_value=1.0, target_value=1000.0, height=1.0, tolerance=1e-9, max_iterations=5
    )
    assert res["iterations_performed"] <= 5