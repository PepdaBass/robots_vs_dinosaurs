from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.battlefield = []
    def run_game(self):
        readied_fleet = Fleet()
        readied_fleet.create_fleet()
        angry_herd = Herd()
        angry_herd.create_herd()
    
    def display_welcome(self):
        user_name = input('Please enter your name, if you dare: ')
        print('''f
        Welcome {user_name} to the ultimate battlefield where an epic fight between robots and
        dinosaurs rages! Prepare yourself for the mayhem and destruction!
        ''')

    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        dino_attack = Herd()

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_oppenent_options(self):
        pass

    def display_winners(self):
        pass

