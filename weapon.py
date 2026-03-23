from item import Item

class Weapon(Item):
    def __init__(self, name, height, price):
        super().__init__(name, height, price)

    def damage_points(self, damage):
        self.damage = damage

    def use(self):
        print(f"You are attacking with {self.name} giving {self.damage} of damage")