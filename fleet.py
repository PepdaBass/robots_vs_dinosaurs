from robot import Robot

class Fleet:
    def __init__(self):
        self.fleet = []
    
    def create_fleet(self):
        robot1 = Robot('X-0')
        robot2 = Robot('X-1')
        robot3 = Robot('X-2')
        self.fleet = (robot1, robot2, robot3)

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