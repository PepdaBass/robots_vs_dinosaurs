from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon('Sword', 25)
   
    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        