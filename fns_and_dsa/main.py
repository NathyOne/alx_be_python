from arithmetic_operations import perform_operation


def main():
    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))
    operation = input("enter operator *,/,+,-: ")
    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")


main()
