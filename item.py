class Item:
    def __init__(self, name, height, price):
        self.name = name
        self.height = height
        self.price = price
    def use(self):
        print("You have {self.name}")