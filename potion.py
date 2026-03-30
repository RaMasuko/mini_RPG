from item import Item
class Potion(Item):
    def __init__(self, name, height, price, cure):
        super().__init__(name, height, price)
        self.cure = cure

    def use(self):
        print(f"You are drinking {self.name} and received {self.cure} of HP!!")
