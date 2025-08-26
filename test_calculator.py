import pytest
from calculator import safe_divide, process_string

# -------------------------------
# Tests for safe_divide
# -------------------------------

@pytest.mark.parametrize(
    "a, b, expected", [
        (6, 2, 3.0),          # regular division
        (5, 0, float('inf')), # division by zero
        (-10, -2, 5.0),       # negative numbers
        (0, 5, 0.0),          # zero numerator
    ]
)
def test_safe_divide(a, b, expected):
    assert safe_divide(a, b) == expected

# Optional: test with float numbers
@pytest.mark.parametrize(
    "a, b, expected", [
        (7.5, 2.5, 3.0),
        (-7.5, 2.5, -3.0)
    ]
)
def test_safe_divide_floats(a, b, expected):
    assert safe_divide(a, b) == expected



@pytest.mark.parametrize(
    "s, action, expected", [
        ("hello", "reverse", "olleh"),
        ("hello", "uppercase", "HELLO"),
        ("HELLO", "lowercase", "hello"),
        ("hello world", "capitalize", "Hello world"),
        ("hello world", "title", "Hello World"),  # title case
    ]
)
def test_process_string_valid(s, action, expected):
    assert process_string(s, action) == expected

# Test invalid action raises ValueError
def test_process_string_invalid_action():
    with pytest.raises(ValueError):
        process_string("hello", "unknown")

# Test non-string input raises TypeError
def test_process_string_invalid_type():
    with pytest.raises(TypeError):
        process_string(123, "uppercase")
