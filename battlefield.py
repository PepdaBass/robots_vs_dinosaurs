from fleet import Fleet
from herd import Herd
import random

class Battlefield:
    def __init__(self):
        self.angry_herd = Herd()
        self.readied_fleet = Fleet()

    # So far run_game has all the fleet and herd information
    def run_game(self):
        self.display_welcome()
        self.readied_fleet.create_fleet()
        self.angry_herd.create_herd()
        self.list_names_of_combatants()
        self.dino_turn(self.angry_herd.herd[0])    
        self.robo_turn(self.readied_fleet.fleet[0])
        self.show_dino_opponent_options() 
        self.show_robo_oppenent_options()
        self.display_winners()  

    # Here is the display screen to begin the battle.    
    def display_welcome(self):
        user_name = input('Please enter your name, if you dare: ')
        print('''
        Welcome ''' + user_name + ''' to the ultimate battlefield where an epic fight between robots and
        dinosaurs rages! Prepare yourself for the mayhem and destruction! You are a captain in charge
        of three robots defending your base from dinosaur infiltration. Command your troops!
        ''')

    # This function throws the names of the combatant objects into a list of strings.
    def list_names_of_combatants(self):
        self.herd_names = [] 
        for dinosaur in self.angry_herd.herd:
            if len(self.herd_names) < 3:
                self.herd_names.append(dinosaur.name)
        print(self.herd_names)

        self.fleet_names = [] 
        for robot_soldier in self.readied_fleet.fleet:
            if len(self.fleet_names) < 3:
                self.fleet_names.append(robot_soldier.name)
        print(self.fleet_names)
    
    def battle(self):
        pass # need to figure out battle tomorrow!!!!!
    
    def dino_turn(self, dinosaur):
        self.dino_stats = []
        self.dino_stats.append(dinosaur.name)
        self.dino_stats.append(dinosaur.health)
        self.dino_stats.append(dinosaur.attack_power)
        print(self.dino_stats)

    def robo_turn(self, robot):
        self.robo_stats = []
        self.robo_stats.append(robot.name)
        self.robo_stats.append(robot.health)
        self.robo_stats.append(robot.weapon.name)
        self.robo_stats.append(robot.weapon.attack_power)
        print(self.robo_stats)

        # for robot_soldier in self.readied_fleet.fleet:
        #     if robot_soldier.name == fleet_names[random.randrange(0-2)]:
        #         print(robot_soldier.name)
        #         break
        
        # for robot_soldier in self.readied_fleet.fleet:
        #     if robot_soldier.weapon.name == 'Sword':
        #         print(robot_soldier.weapon.name)
        #         break

    def show_dino_opponent_options(self):
        display_stats = False
        index = 0
        while display_stats is False:
            if index == 0:
                print(f'Name: {self.dino_stats[0]}')
                index += 1
            elif index == 1:
                print(f'Health: {self.dino_stats[1]}')
                index += 1
            elif index == 2:
                print(f'Attack Power: {self.dino_stats[2]}')
                break
        # Index[0] will always be 'Name', index[1] Health, and index[2] attack power.

    def show_robo_oppenent_options(self):
        display_stats = False
        index = 0
        while display_stats is False:
            if index == 0:
                print(f'Name: {self.robo_stats[0]}')
                index += 1
            elif index == 1:
                print(f'Health: {self.robo_stats[1]}')
                index += 1
            elif index == 2:
                print(f'Weapon: {self.robo_stats[2]}')
                index += 1
            elif index == 3:
                print(f'Attack Power: {self.robo_stats[3]}')
                break
        # Index[0] will always be 'Name', index[1] Health, index[2] weapon, and index[3] attack power.

    def display_winners(self):
        if len(self.herd_names) > 0:
            for dinosaurs in self.herd_names:
                print(dinosaurs)
        elif len(self.fleet_names) > 0:
            for robots in self.fleet_names:
                print(robots)

