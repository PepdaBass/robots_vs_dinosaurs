from robot import Robot

class Fleet:
    def __init__(self):
        self.fleet = []
        self.robot1 = Robot('X-0')
        self.robot2 = Robot('X-1')
        self.robot3 = Robot('X-2')

    # Hardcoded the robots into the fleet. Maybe I'll use a while loop later.
    def create_fleet(self):
        self.fleet.append(self.robot1)
        self.fleet.append(self.robot2)
        self.fleet.append(self.robot3)

        
        
        
        
        
        # robot_designation_number = 0
        # fleet_total = False
        # while fleet_total is False:
        #     if robot_designation_number <= 2:
        #         robot_soldier = Robot(f'X-{robot_designation_number}')
        #         self.fleet.append(robot_soldier)
        #         robot_designation_number += 1
        #     else:
        #         fleet_total is True
        #         break