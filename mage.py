from entity import Entity

class Mage(Entity):
    def attack(self): 
        print ("The mage used a fire ball! 50 of damage")
        return 50