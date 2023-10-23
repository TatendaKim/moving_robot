import random



#global variable
position_obstacles = []    

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

# if position (x,y) falls inside an obstacle
def is_position_blocked(x,y):
    """Checks if there is a direct colision with the obstacle and the robots end location
    """
    for (p,q) in position_obstacles:
        if x in range(p,p+4) and y in range(q,q+4):
            print("Sorry, there is an obstacle in the way.")
            return True
    return False


#  if there is an obstacle in the line between the coordinates (x1, y1) and (x2, y2).
def is_path_blocked(x1,y1, x2, y2, obstacle_list):
    """_These function will restrict the robot to not move through the obstacles_

    Args:
        x1 (_int_): _start point of x-value_
        y1 (_int_): _start point of x-value_
        x2 (_int_): _end point of x-value_
        y2 (_int_): _end point of y-value_

    Returns:
        _bool_: _description_
    """
    if_blocked_list = []

    if x1 > x2:
        x1, x2 = x2, x1
    elif y1 > y2:
        y1, y2 = y2, y1

    for obstacle in obstacle_list:
        ob_x, ob_y = obstacle

        for i in range(4):
            if_blocked_list.append(True if ob_x in range(x1, x2 + 1) and ob_y in range(y1, y2 + 1) else False)
            ob_x += 1
            ob_y += 1
        ob_x, ob_y = obstacle

    return True if True in if_blocked_list else False


    # if x1 == x2:
    #     y_range = range(y2,y1)
    #     if y1 < y2:
    #         y_range = (y1,y2)
    #     for i in y_range:
    #         if is_position_blocked(x1,i):
    #             return True
    
    # if y1 == y2:
    #     x_range = range(x2,x1)
    #     if x1 < x2:
    #         x_range = (x1,x2)
    #     for i in x_range:
    #         if is_position_blocked(y1,i):
    #             return True
    return False





def get_obstacles():
    global position_obstacles
    """_These function will generate random numbers append them to tuple list_

    Returns:
        _list_: _obstacles_
    """
    position_obstacles = [(random.randint(-200, 200),random.randint(-400, 400)) for _ in range(random.randint(0,10))]
    # print(position_obstacles)
    return position_obstacles, position_obstacles
# get_obstacles()


