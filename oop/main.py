from enemy import Enemy
from zombie import Zombie
from ogre import Ogre

zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

print(
    f"{zombie.get_type_of_enemy()} has {zombie.health_points} health points and {zombie.attack_damage} attack damage"
)

print(
    f"{ogre.get_type_of_enemy()} has {ogre.health_points} health points and {ogre.attack_damage} attack damage"
)

zombie.talk()
ogre.talk()
