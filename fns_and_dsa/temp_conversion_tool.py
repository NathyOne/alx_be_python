FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    result = FAHRENHEIT_TO_CELSIUS_FACTOR*fahrenheit
    print(f"{fahrenheit}°F: {result}°C")


def convert_to_fahrenheit(celsius):
    result = CELSIUS_TO_FAHRENHEIT_FACTOR*celsius
    print(f"{celsius}°C: {result}°F")


def main():
    temp = float(input("Enter the temperature to convert: "))
    if isinstance(temp, str):
        print("the temperature must be a number")
        return None
    choice = input(
        "Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if choice == "C":
        convert_to_fahrenheit(temp)
    elif choice == "F":
        convert_to_celsius(temp)
    else:
        print("Incorrect choice")


main()
