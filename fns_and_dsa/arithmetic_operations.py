def perform_operation(num1, num2, operation):

    if operation == "add":
        print(num1 + num2)
    elif operation == "subtract":
        print(num1-num2)
    elif operation == "multiply":
        print(num1*num2)
    elif operation == "divide":
        if num2 == 0:
            return print("can't divide by 0")
    else:
        return print("unknown operation")
