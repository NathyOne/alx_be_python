def perform_operation(num1, num2, operation):
    match operation:
        case "+":
            print(num1 + num2)
        case "-":
            print(num1 - num2)
        case "/":
            if num2 == 0:
                print("can't divide by zero")
            else:
                print(num1 / num2)
        case "*":
            print(num1 * num2)
