def perform_operation(num1: float, num2: float, operation: str):
    match operation:
        case "+":
            result = num1 + num2
            print(result)
            return result
        case "-":
            result = num1 - num2
            print(result)
            return result
        case "/":
            if num2 == 0:
                print("can't divide by zero")
                return None
            else:
                result = num1 / num2
                print(result)
                return result
        case "*":
            result = num1 * num2
            print(result)
            return result
        case _:
            print(f"Unknown operation: {operation}")
            return None
