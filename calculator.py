# Advanced Function Testing Module

def safe_divide(a: float, b: float) -> float:
    """
    Divides a by b, handling division by zero.
    Returns 'inf' if b == 0.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')


def process_string(s: str, action: str) -> str:
    """
    Processes a string based on the action parameter.
    Available actions: 'reverse', 'uppercase', 'lowercase', 'capitalize'.
    Raises ValueError for invalid actions.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    if action == "reverse":
        return s[::-1]
    elif action == "uppercase":
        return s.upper()
    elif action == "lowercase":
        return s.lower()
    elif action == "capitalize":
        return s.capitalize()
    elif action == "title":
        return s.title()
    else:
        raise ValueError("Invalid action provided")
