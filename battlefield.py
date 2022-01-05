from fleet import Fleet
from herd import Herd
import random

class Battlefield:
    def __init__(self):
        self.angry_herd = Herd()
        self.readied_fleet = Fleet()

    def run_game(self):
        # self.display_welcome()
        self.readied_fleet.create_fleet()
        self.angry_herd.create_herd()
        self.list_names_of_combatants()
        self.versus_battle_stats()
        self.battle() 

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
        ultimate_victory = False
        while ultimate_victory is False:
            if len(self.herd_names) < 1 or len(self.fleet_names) < 1:
                ultimate_victory = True
                self.display_winners()
            elif len(self.herd_names) > 0 or len(self.fleet_names) > 0:
                battle_counter = 0
                attack_attempt = False
                while attack_attempt is False:
                    self.correct_opponent_health()
                    if self.dino_stats[1] < 1 or self.robo_stats[1] < 1:
                        self.opponent_death
                        attack_attempt = True
                    elif battle_counter == 0:
                        self.show_robo_oppenent_options()
                        self.readied_fleet.fleet[0].attack(self.angry_herd.herd[self.correct_dino_index])
                        battle_counter += 1
                        self.versus_battle_stats()
                        self.opponent_death()
                    elif battle_counter % 2 != 0:
                        self.show_dino_opponent_options()
                        self.angry_herd.herd[0].attack(self.readied_fleet.fleet[self.correct_robot_index])
                        battle_counter +=1
                        self.versus_battle_stats()
                        self.opponent_death()
                    elif battle_counter % 2 == 0:
                        self.show_robo_oppenent_options
                        self.readied_fleet.fleet[0].attack(self.angry_herd.herd[self.correct_dino_index])
                        battle_counter += 1
                        self.versus_battle_stats()
                        self.opponent_death()

     # Makes sure the correct opponents health is being modified by that attacks in the battle.           
    def correct_opponent_health(self):
        if len(self.fleet_names) == 3:
            self.correct_robot_index = 0
        elif len(self.fleet_names) == 2:
            self.correct_robot_index = 1
        elif len(self.fleet_names) == 1:
            self.correct_robot_index = 2

        if len(self.herd_names) == 3:
            self.correct_dino_index = 0
        elif len(self.herd_names) == 2:
            self.correct_dino_index = 1
        elif len(self.herd_names) == 1:
            self.correct_dino_index = 2
   
    # Checks to see if health is equal to zero or below and, if so, pops the name out of herd_names
    # or fleet_names so that I can move onto the next opponent in the list via versus_battle_stats().
    def opponent_death(self):
        self.loser = ''
        if self.dino_stats[1] <= 0:
            print(f'{self.herd_names[0]} was killed.')
            print(' ')
            self.loser = self.herd_names.pop(0)
            self.versus_battle_stats()
        elif self.robo_stats[1] <= 0:
            print(f'{self.fleet_names[0]} was killed.')
            print(' ')
            self.loser = self.fleet_names.pop(0)
            self.versus_battle_stats()
        else:
            self.versus_battle_stats()
            
    # This ensures that each robot or dinosaur is cycled to after one dies and its stats are printed.
    def versus_battle_stats(self):
        versus_battle_dino = False
        while versus_battle_dino is False:
            if len(self.herd_names) == 3:
                self.dino_turn(self.angry_herd.herd[0])
                versus_battle_dino = True
            elif len(self.herd_names) == 2:
                self.dino_turn(self.angry_herd.herd[1])
                versus_battle_dino = True
            elif len(self.herd_names) == 1:
                self.dino_turn(self.angry_herd.herd[2])
                versus_battle_dino = True
            elif len(self.herd_names) < 1:
                versus_battle_dino = True
                self.display_winners()
            print(' ')
            print('Current Stats:')
            self.show_dino_opponent_options()
            print(' ')
        versus_battle_robot = False
        while versus_battle_robot is False:
            if len(self.fleet_names) == 3:
                self.robo_turn(self.readied_fleet.fleet[0])
                versus_battle_robot = True
            elif len(self.fleet_names) == 2:
                self.robo_turn(self.readied_fleet.fleet[1])
                versus_battle_robot = True
            elif len(self.fleet_names) == 1:
                self.robo_turn(self.readied_fleet.fleet[2])
                versus_battle_robot = True
            elif len(self.fleet_names) < 1:
                versus_battle_robot = True
                self.display_winners()
            self.show_robo_oppenent_options()
            print(' ')
    
    def dino_turn(self, dinosaur):
        self.dino_stats = []
        self.dino_stats.append(dinosaur.name)
        self.dino_stats.append(dinosaur.health)
        self.dino_stats.append(dinosaur.attack_power)
        # print(self.dino_stats)

    def robo_turn(self, robot):
        self.robo_stats = []
        self.robo_stats.append(robot.name)
        self.robo_stats.append(robot.health)
        self.robo_stats.append(robot.weapon.name)
        self.robo_stats.append(robot.weapon.attack_power)
        # print(self.robo_stats)

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
        if len(self.fleet_names) < 1:
            print('The victors are:')
            for dinosaurs in self.herd_names:
                print(dinosaurs)
        elif len(self.herd_names) < 1:
            print('The victors are:')
            for robots in self.fleet_names:
                print(robots)

