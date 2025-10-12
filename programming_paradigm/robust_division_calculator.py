def safe_divide(numerator, denominator):
    try:
        return float(numerator) / float(denominator)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except (ValueError, TypeError):
        return "Error: Non-numeric input provided"
