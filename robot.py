from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon('Sword', 25)

    # I'm not feeling super comfortable with this being the attack method...    
    def attack(self, dinosaur):
        attack_strength = self.weapon.attack_power
        dinosaur += -(attack_strength)