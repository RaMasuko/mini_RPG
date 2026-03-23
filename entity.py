class Entity:
    def __init__(self, name, life=100): 
        self.name = name
        self.life = life

    def damage(self, damage):
        self.life -= damage
        print(f"{self.name} took {damage} damage! Life: {self.life}")

    def attack(self): 
        print("Generic attack! 10 damage")
        return 10