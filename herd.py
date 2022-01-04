from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.herd = []
        self.dino1 = Dinosaur('T-Rex', 100)
        self.dino2 = Dinosaur('Velociraptor', 65)
        self.dino3 = Dinosaur('Stegosaurus', 75)

    # Hardcoded the dinos the same as I did the robots.
    def create_herd(self):
        self.herd.append(self.dino1)
        self.herd.append(self.dino2)
        self.herd.append(self.dino3)