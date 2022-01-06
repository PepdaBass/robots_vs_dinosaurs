from fleet import Fleet
from herd import Herd
import random

class Battlefield:
    def __init__(self):
        self.angry_herd = Herd()
        self.readied_fleet = Fleet()

    def run_game(self):
        self.display_welcome()
        self.readied_fleet.create_fleet()
        self.angry_herd.create_herd()
        self.list_names_of_combatants()
        self.versus_battle_stats()
        self.battle()
        self.display_winners()

    # Here is the display screen to begin the battle.    
    def display_welcome(self):
        user_name = input('Please enter your name, if you dare: ')
        print('''
        Welcome ''' + user_name + ''' to the ultimate battlefield where an epic fight between robots and
        dinosaurs rages! Prepare yourself for the mayhem and destruction! You are a captain in charge
        of three robots defending your base from dinosaur infiltration. Command your troops!

        The first wave is a Tyrannosaurus Rex!
        ''')

    # This function throws the names of the combatant objects into lists of strings.
    def list_names_of_combatants(self):
        self.herd_names = [] 
        for dinosaur in self.angry_herd.herd:
            if len(self.herd_names) < 3:
                self.herd_names.append(dinosaur.name)
       

        self.fleet_names = [] 
        for robot_soldier in self.readied_fleet.fleet:
            if len(self.fleet_names) < 3:
                self.fleet_names.append(robot_soldier.name)
        
    # This is all the fighting logic. Robots and dinosaurs alternate turns and have a chance of hitting or missing
    # during an attack sequence. The user is expected to hit 'Enter' before each turn is taken so that the user can
    # follow the action.
    def battle(self):
        battle_counter = 0
        attack_attempt = False
        while attack_attempt is False:
            self.correct_opponent_health()
            self.attack_success = random.randrange(0, 10)
            if len(self.herd_names) == 0 or len(self.fleet_names) == 0:
                attack_attempt = True
            elif battle_counter == 0 or battle_counter % 2 == 0:
                print(input('Command your fleet! Press Enter to attack: '))
                if self.attack_success <=3:
                    print('Your robot malfunctioned and missed!')
                    battle_counter += 1
                    self.versus_battle_stats()
                    self.opponent_death()
                    continue
                elif self.attack_success >= 4:
                    print('Your robot scores a hit!')
                    self.readied_fleet.fleet[self.correct_robot_index].attack(self.angry_herd.herd[self.correct_dino_index])
                    battle_counter += 1
                    self.versus_battle_stats()
                    self.opponent_death()
            elif battle_counter % 2 != 0:
                print(input('The dinosaurs are attacking! Prepare to defend by pressing Enter: '))
                if self.attack_success <=6:
                    print('You dodged the dinosaur attack!')
                    battle_counter += 1
                    self.versus_battle_stats()
                    self.opponent_death()
                    continue
                elif self.attack_success >= 7:
                    print('The dinosaur hits the robot...')
                    self.angry_herd.herd[self.correct_dino_index].attack(self.readied_fleet.fleet[self.correct_robot_index])
                    battle_counter += 1
                    self.versus_battle_stats()
                    self.opponent_death()
     
     
     # Makes sure the correct opponents health is being modified by the attacks in the battle.           
    def correct_opponent_health(self):
        if len(self.fleet_names) == 3:
            self.correct_robot_index = 0
        elif len(self.fleet_names) == 2:
            self.correct_robot_index = 1
        elif len(self.fleet_names) == 1:
            self.correct_robot_index = 2
        else:
            pass

        if len(self.herd_names) == 3:
            self.correct_dino_index = 0
        elif len(self.herd_names) == 2:
            self.correct_dino_index = 1
        elif len(self.herd_names) == 1:
            self.correct_dino_index = 2
        else:
            pass
   
    # Checks to see if health is equal to zero or below and, if so, pops the name out of herd_names
    # or fleet_names so that I can move onto the next opponent in the list via versus_battle_stats() below.
    def opponent_death(self):
        self.loser = ''
        if self.dino_stats[1] <= 0:
            print(f'{self.herd_names[0]} was annihilated.')
            print(' ')
            if len(self.herd_names) == 0:
                pass
            elif len(self.herd_names) >= 1:
                self.loser = self.herd_names.pop(0)
                self.versus_battle_stats()
        elif self.robo_stats[1] <= 0:
            print(f'{self.fleet_names[0]} was destroyed.')
            print(' ')
            if len(self.fleet_names) == 0:
                pass
            elif len(self.fleet_names) >= 1:
                self.loser = self.fleet_names.pop(0)
                self.versus_battle_stats()
            
    # This ensures that each robot or dinosaur is cycled to after one dies and its stats are printed.
    def versus_battle_stats(self):
        versus_battle_dino = False
        while versus_battle_dino is False:
            if len(self.fleet_names) == 0 or len(self.herd_names) == 0:
                versus_battle_dino = True
            elif len(self.herd_names) == 3:
                self.dino_turn(self.angry_herd.herd[0])
                versus_battle_dino = True
                print(' ')
                print('Current Stats:')
                self.show_dino_opponent_options()
                print(' ')
            elif len(self.herd_names) == 2:
                self.dino_turn(self.angry_herd.herd[1])
                versus_battle_dino = True
                print(' ')
                print('Current Stats:')
                self.show_dino_opponent_options()
                print(' ')
            elif len(self.herd_names) == 1:
                self.dino_turn(self.angry_herd.herd[2])
                versus_battle_dino = True
                print(' ')
                print('Current Stats:')
                self.show_dino_opponent_options()
                print(' ')
    
        versus_battle_robot = False
        while versus_battle_robot is False:
            if len(self.herd_names) == 0 or len(self.fleet_names) == 0:
                versus_battle_robot = True
            elif len(self.fleet_names) == 3:
                self.robo_turn(self.readied_fleet.fleet[0])
                versus_battle_robot = True
                self.show_robo_oppenent_options()
                print(' ')
            elif len(self.fleet_names) == 2:
                self.robo_turn(self.readied_fleet.fleet[1])
                versus_battle_robot = True
                self.show_robo_oppenent_options()
                print(' ')
            elif len(self.fleet_names) == 1:
                self.robo_turn(self.readied_fleet.fleet[2])
                versus_battle_robot = True
                self.show_robo_oppenent_options()
                print(' ')
           
    # Appends all dinosaur attributes to a list.
    def dino_turn(self, dinosaur):
        self.dino_stats = []
        self.dino_stats.append(dinosaur.name)
        self.dino_stats.append(dinosaur.health)
        self.dino_stats.append(dinosaur.attack_power)

    # Appends all robot object attributes to a list.
    def robo_turn(self, robot):
        self.robo_stats = []
        self.robo_stats.append(robot.name)
        self.robo_stats.append(robot.health)
        self.robo_stats.append(robot.weapon.name)
        self.robo_stats.append(robot.weapon.attack_power)

    # Index[0] will always be 'Name', index[1] Health, and index[2] attack power.
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
        
    # Index[0] will always be 'Name', index[1] Health, index[2] weapon, and index[3] attack power.
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

    # Prints the names of the surviving victors of the battle.
    def display_winners(self):
        if len(self.fleet_names) == 0:
            print('The victors are:')
            for dinosaurs in self.herd_names:
                print(dinosaurs)
        elif len(self.herd_names) == 0:
            print('The victors are:')
            for robots in self.fleet_names:
                print(robots)

