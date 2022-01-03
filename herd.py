from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.herd = []

    def create_herd(self):
        dino1 = Dinosaur('T-Rex')
        dino2 = Dinosaur('Velocirapto')
        dino3 = Dinosaur('Stegosaurus')
        self.fleet = (dino1, dino2, dino3)