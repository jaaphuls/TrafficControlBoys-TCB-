# this script contains the code to run the random algorithm
from code.classes.board import self.car_list 
from code.classes.board import check_move
from code.classes.vehicle import location_vehicle


def random_step(self): 

    car = random.choice(self.car_list)

    able_to_move = check_move(car)
    (left_up, right_down) = able_to_move

    # check in what orientation the car should move
    if car.orientation == 'H': 

        # give a chance of 0.5 to either move towards the right or left
        if random.randint(1, 2) != 1:
            if right_down == True:  
                car.x += 1 
        else: 
            if left_up == True: 
                car.x -= 1
    
    # if the orientation is not horizontal, move on the y-axis
    else: 

        # give the same chance of 0.5 to move towards the top or the bottom
        if random.randint(1, 2) != 1: 
            if left_up == True: 
                car.y += 1 
        else: 
            if right_down == True: 
                car.y -= 1

    car.location_vehicle()
    

