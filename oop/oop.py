import csv


class Item:
    all = []

    def __init__(self, name, price: float, quantity: int):

        assert price >= 1, f"the price must be greater than or equals to 1"
        assert quantity >= 0,  f"the quantity can be zero but not negative"
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def total_price_of_items(self):
        return self.price*self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get("name").strip(),
                price=float(item.get("price").strip()),
                quantity=int(item.get("quantity").strip())
            )

    def __repr__(self):
        return f"{self.name} {self.price} {self.quantity}"


Item.instantiate_from_csv()
print(Item.all)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_person(self):
        print(f"I'm {self.name} and i'm {self.age} years of age")

    def __del__(self):
        print(f"person {self.name} is destroyed")


p1 = Person("Nati", 25)
p1.print_person()


class belachew(Person):
    def print__person(self):
        print("child class method")


b1 = belachew("bela", 24)
print(b1.print__person())


class Book:
    def __init__(self, author, title, pages: int):
        self.author = author
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"The Book is: {self.title}, The Author is {self.author} and it have {self.pages} pages"

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.pages})"


b1 = Book("cal newport", "Deep work", 400)
print(b1)
print(repr(b1))

exercise-0 on oop


class animal:
    def make_sound(self):
        print("all animals make different sound")


class Dog(animal):
    def make_sound(self):
        print("woof!")


animals = [Dog(), animal()]

for animal in animals:
    print(animal.make_sound())

exercise-1 on oop


class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width*self.height


rect = Rectangle(3, 4)


print(f"The are of the rectangle is {rect.calculate_area()}")

exercise 3 oop


class bird:
    def fly(self):
        return "I can fly"


class mammals:
    def run(self):
        return "I can run"


class bat(bird, mammals):
    pass


bat1 = bat()

print(bat1.fly())
print(bat1.run())


class Dog:
    def make_sound(self):
        return "woof"


class Cat:
    def make_sound(self):
        return "meow"


class Bird:
    def make_sound(self):
        return "quack"


def let_them_speak(obj):
    return obj.make_sound()


d1 = Dog()
c1 = Cat()
b1 = Bird()

print(let_them_speak(d1))


class methods


WE use class methods when we want to work around the class itself and any instances that are at the class level


class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def print_total_count(cls):
        return print(f"total number of people is {cls.count}")


obj1 = Person("tade")
obj2 = Person("Nathy")

Person.print_total_count()


class animals:
    count = 0

    def __init__(self, name):
        self.name = name
        animals.count += 1

    def count_animals(self):
        return f"total animals: {animals.count}"


obj1 = animals("lion")
obj2 = animals("rabbit")

print(obj1.count_animals())
