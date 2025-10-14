# static and class methods


# class methods
class Book:
    count = 0

    def __init__(self, title, author):
        self.title = title
        self.author = title
        Book.count += 1

    @classmethod
    def total_count(cls):
        return f"the total number of books is: {cls.count}"


b1 = Book("book-1", "p-1")
b2 = Book("book-2", "p-2")
b2 = Book("book-3", "p-3")

print(Book.total_count())

# static-methods
# no need to create an instance


class Calculator:

    @staticmethod
    def add(x, y):
        return x+y

    @staticmethod
    def mul(x, y):
        return x*y

    @staticmethod
    def sub(x, y):
        return x-y

    @staticmethod
    def div(x, y):
        return x/y


print(Calculator.add(5, 8))


# more on class-methods

class child:
    inital_age = 0

    def __init__(self, name):
        self.name = name

    @classmethod
    def create_child(cls):
        return f"new born {cls.inital_age} years old"


ch1 = child("babi")

print(f"the child name is {ch1.name}, {ch1.create_child()}")
