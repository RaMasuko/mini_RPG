from item import Item
class Potion(Item):
    def __init__(self, name, height, price):
        super().__init__(name, height, price)

    def cure_points (self, cure):
        self.cure = cure

    def use(self):
        print(f"You are drinking {self.name} and received {self.cure} of HP!!")