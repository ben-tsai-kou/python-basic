from enemy import Enemy
import random


class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(
            type_of_enemy="Zombie",
            health_points=health_points,
            attack_damage=attack_damage,
        )

    def talk(self):
        print("Brains...")

    def spread_disease(self):
        print("Zombie spreads disease.")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.50
        if did_special_attack_work:
            self.health_points += 2
            print(f"Zombie regenerated 2 HP.")
