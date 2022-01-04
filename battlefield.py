from fleet import Fleet
from herd import Herd
import random

class Battlefield:
    def __init__(self):
        self.battlefield = []
        self.angry_herd = Herd()
        self.readied_fleet = Fleet()

    # So far run_game has all the fleet and herd information
    def run_game(self):
        self.readied_fleet.create_fleet()
        self.angry_herd.create_herd()
        for robot_soldier in self.readied_fleet.fleet:
            if robot_soldier.name != 'X-1':
                continue
            print(robot_soldier.name)

        for robot_soldier in self.readied_fleet.fleet:
            if robot_soldier.weapon.name == 'Sword':
                print(robot_soldier.weapon.name)
                break
           
           
                

    # Here is the display screen to begin the battle.    
    def display_welcome(self):
        user_name = input('Please enter your name, if you dare: ')
        print('''f
        Welcome {user_name} to the ultimate battlefield where an epic fight between robots and
        dinosaurs rages! Prepare yourself for the mayhem and destruction!
        ''')

    def battle(self):
        pass

    # To be able to pull off attacks, I need to access attributes in the object lists.
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

