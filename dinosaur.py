class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    # I'm not feeling super comfortable with this being the attack method... 
    def attack(self, robot):
        attack_strength = self.attack_power
        robot += -(attack_strength)