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


item1 = Item("Iphone-17", 2000, 5)
item2 = Item("samsung s24 ultra", 1200, 13)
item3 = Item("Iphone-16", 1000, 6)
item4 = Item("black-berry", 700, 4)
item5 = Item("google pixel", 900, 9)


for item in Item.all:
    print(
        f"The Item Name: {item.name}, The price is: {item.price}, Item Quantity is: {item.quantity}")
