class Item:
    # ctor

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


# instance1
item1 = Item("Phone", 100, 5)


# instance2
item2 = Item("Laptop", 1000, 3)


print(item1.name)
print(item2.name)
