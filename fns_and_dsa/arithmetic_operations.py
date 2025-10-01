def perform_operation(num1: float, num2: float, operation: str):
    match operation:
        case "+":
            print(num1 + num2)
        case "-":
            print(num1 - num2)  # Also fixed: was adding instead of subtracting
        case "/":
            if num2 == 0:
                print("can't divide by zero")
            else:
                print(num1 / num2)
        case "*":
            return num1 * num2
