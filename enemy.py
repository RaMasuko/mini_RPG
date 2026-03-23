from entity import Entity

class Enemy(Entity):
    def attack(self):
        return super().attack() + 3
    def attack(self):
        pass