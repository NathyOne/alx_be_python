import os


# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_info(self):
#         return f"my name is {self.name} and i'm {self.age} years old"


# st1 = student("samuel", 22)

# print(f"{st1.display_info()}")


# def division_handler(num1, num2):
#     if num2 == 0:
#         raise ZeroDivisionError
#     else:
#         print
#         return num1/num2


# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# result = division_handler(num1, num2)

# print(f"the result from the division is {result}")


# directory = "/intro/java"


# def fileNotFoundException(file):
#     file_path = os.path.join(directory, file)

#     if os.path.exists(file_path):
#         print("file exist")
#     else:
#         raise FileNotFoundError(
#             f"File '{file}' not found in directory '{directory}'")


# file = input("enter the file name: ")

# fileNotFoundException(file)


class ValueTooHighError(Exception):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"ValueTooHighError: {self.num} is too high"


num = int(input("enter a number"))

if num > 100:
    raise ValueTooHighError(num)
else:
    print("OK")
