def safe_divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except (ValueError, TypeError):
        return "Non-numeric input provided"
    

