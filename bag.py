from potion import Potion
from weapon import Weapon

bag = [
    Potion("Pocao de Cura", 500 , 10),
    Weapon("Sword", 1000, 100)
]
for Item in bag:
    Item.use()