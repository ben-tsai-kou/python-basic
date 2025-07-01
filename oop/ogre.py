from enemy import Enemy
import random


class Ogre(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(
            type_of_enemy="Ogre",
            health_points=health_points,
            attack_damage=attack_damage,
        )

    def talk(self):
        print("*gruff growl*")

    def walk_forward(self):
        print("Ogre moves closer to you.")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.20
        if did_special_attack_work:
            self.attack_damage += 4
            print(f"Ogre gets angry and increases attack by 4.")
