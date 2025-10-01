from arithmetic_operations import perform_operation


def main():
    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))
    operator = input("enter operator *,/,+,-: ")
    result = perform_operation(num1, num2, operator)
    print(f"Result: {result}")


main()
