# import csv


# class Item:
#     all = []

#     def __init__(self, name, price: float, quantity: int):

#         assert price >= 1, f"the price must be greater than or equals to 1"
#         assert quantity >= 0,  f"the quantity can be zero but not negative"
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         Item.all.append(self)

#     def total_price_of_items(self):
#         return self.price*self.quantity

#     @classmethod
#     def instantiate_from_csv(cls):
#         with open('items.csv', 'r') as f:
#             reader = csv.DictReader(f)
#             items = list(reader)
#         for item in items:
#             Item(
#                 name=item.get("name").strip(),
#                 price=float(item.get("price").strip()),
#                 quantity=int(item.get("quantity").strip())
#             )

#     def __repr__(self):
#         return f"{self.name} {self.price} {self.quantity}"


# Item.instantiate_from_csv()
# print(Item.all)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def print_person(self):
#         print(f"I'm {self.name} and i'm {self.age} years of age")

#     def __del__(self):
#         print(f"person {self.name} is destroyed")


# p1 = Person("Nati", 25)
# p1.print_person()


# class belachew(Person):
#     def print__person(self):
#         print("child class method")


# b1 = belachew("bela", 24)
# print(b1.print__person())


# class Book:
#     def __init__(self, author, title, pages: int):
#         self.author = author
#         self.title = title
#         self.pages = pages

#     def __str__(self):
#         return f"The Book is: {self.title}, The Author is {self.author} and it have {self.pages} pages"

#     def __repr__(self):
#         return f"Book({self.title}, {self.author}, {self.pages})"


# b1 = Book("cal newport", "Deep work", 400)
# print(b1)
# print(repr(b1))


class animal:
    def make_sound(self):
        print("all animals make different sound")


class Dog(animal):
    def make_sound(self):
        print("woof!")


animals = [Dog(), animal()]

for animal in animals:
    print(animal.make_sound())
