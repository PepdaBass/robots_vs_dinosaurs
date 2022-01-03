from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.herd = []

    # Hardcoded the dinos the same as I did the robots.
    def create_herd(self):
        dino1 = Dinosaur('T-Rex', 100)
        dino2 = Dinosaur('Velocirapto', 65)
        dino3 = Dinosaur('Stegosaurus', 75)
        self.herd = (dino1, dino2, dino3)