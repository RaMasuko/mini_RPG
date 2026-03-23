from entity import Entity

class Warrior(Entity):
    def __init__(self, name, strength, life = 150):
        super().__init__(name, life)
        self.strength = strength

    def attack(self):
        print (f"LANCE ATACK!!! {self.strength}")
        return self.strength