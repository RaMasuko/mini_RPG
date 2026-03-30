from item import Item
from magic import Magic

class Weapon(Item, Magic):
    def __init__(self, name, height, price, damage):
        super().__init__(name, height, price)
        self.damage = damage

    def use(self):
        self.shiny()
        print(f"You are attacking with {self.name} giving {self.damage} of damage")
