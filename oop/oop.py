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
                name=item.get("name"),
                price=int(item.get("price")),
                quantity=int(item.get("quantity"))
            )


Item.instantiate_from_csv()
print(Item.all)
