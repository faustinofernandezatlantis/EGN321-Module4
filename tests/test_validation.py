from src.validation import validate_inputs


def test_invalid_negative_initial_value():
    is_valid, msg = validate_inputs(-1.0, 100.0, 5.0, 1e-3, 50)
    assert is_valid is False
    assert "positive" in msg.lower()


def test_invalid_max_iterations():
    is_valid, msg = validate_inputs(1.0, 100.0, 5.0, 1e-3, 0)
    assert is_valid is False