from entity import Entity

class Boss(Entity):
    def damage(self, damage):
        real_damage = damage/2
        super().damage(real_damage)
        print ("Hahahah!! Loser")