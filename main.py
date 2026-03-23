from boss import Boss
from dragon import Dragon
from enemy import Enemy
from mage import Mage
from warrior import Warrior

main_warrior = Warrior("Warrior", 30, 200)

print (f"Main Warrior name is {main_warrior.name}")

print (f"Main Warrior life is {main_warrior.life}")

main_warrior.damage(32)

main_mage = Mage("Merlin", 100)

slime = Enemy("Slime", 200)

slime.damage(main_mage.attack())
slime.damage(main_warrior.attack())

obelisco = Boss("Obelisco", 150)

obelisco.damage(main_mage.attack())

banguela = Dragon("Banguela", 500)

banguela.fly()

main_mage.damage(banguela.attack())

print(Dragon.mro())