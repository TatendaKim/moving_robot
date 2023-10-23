position_obstacles = []
maze_points = []
# # if position (x,y) falls inside an obstacle
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
            if_blocked_list.append(True if ob_x in range(x1, x2) and ob_y in range(y1, y2) else False)
            ob_x += 1
            ob_y += 1
        ob_x, ob_y = obstacle

    return True if True in if_blocked_list else False
    

grid = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X               X                                 X",
"X  XXXXXXXXXX  XXXXXXXXXXXXX  XXXXXXX  XXXXXXXXXXXX",
"X           X                 X               XX  X",
"X  XXXXXXX  XXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX  X",
"X  X     X  X           X  X                 XXX  X",
"X  X  X  X  X  X  XXXX  X  X  XXXXXXXXXXXXX  XXX  X",
"X  X  X  X  X  X  X        X  X  X        X       X",
"X  X  XXXX  X  XXXXXXXXXX  X  X  XXXX  X  X  XX   X",
"X  X     X  X          X   X           X  X  XX  XX",
"X  XXXX  X  XXXXXXX XXXXXXXX  XXXXXXXXXXXXX  XX  XX",
"X     X  X     X              X              XX   X",
"XXXX  X  XXXXXXXXXX XXXXXXXXXXX  XXXXXXXXXX  XXX  X",
"X  X  X                    X     X     X  X  XXX  X",
"X  X  XXXX  XXXXXXXXXXXXX  X  XXXX  X  X  X  XX   X",
"X  X  X     X     X     X  X  X     X     X  XX  XX",
"X  X  X  XXXXXXX  XXXX  X  X  X  XXXXXXXXXX  XX  XX",
"X                       X  X  X              XX  XX",
"X XXXXXX             X  X  X  X  XXX        XXX  XX",
"X XXXXXX XXXXXX XXXXXXXXX    XX XX   XXXXXXXXXX  XX",
"X X    X    XXX X     XXXXXXXXX XX  XXXXXXX    X XX",
"X XXXX XXXX XXX X XXX XXX    XX    XX    XX XX X XX",
"X XXXX    X     X XXX XXX XX XXXXXXXX XX XX XX   XX",
"X      XX XXXXXXXeXXX     XX          XX    XXXXXXX",
"X               X                                 X",
"X  XXXXXXXXXX  XXXXXXXXXXXXX  XXXXXXX  XXXXXXXXXXXX",
"Xs          X                 X               XX  X",
"X  XXXXXXX  XXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX  X",
"X  X     X  X           X  X                 XXX  X",
"X  X  X  X  X  X  XXXX  X  X  XXXXXXXXXXXXX  XXX  X",
"X  X  X  X  X  X  X        X  X  X        X       X",
"X  X  XXXX  X  XXXXXXXXXX  X  X  XXXX  X  X  XX   X",
"X  X     X  X          X   X           X  X  XX  XX",
"X  XXXX  X  XXXXXXX XXXXXXXX  XXXXXXXXXXXXX  XX  XX",
"X     X  X     X              X              XX   X",
"XXXX  X  XXXXXXXXXX XXXXXXXXXXX  XXXXXXXXXX  XXX  X",
"X  X  X                    X     X     X  X  XXX  X",
"X  X  XXXX  XXXXXXXXXXXXX  X  XXXX  X  X  X  XX   X",
"X  X  X     X     X     X  X  X     X     X  XX  XX",
"X  X  X  XXXXXXX  XXXX  X  X  X  XXXXXXXXXX  XX  XX",
"X                       X  X  X              XX  XX",
"X XXXXXX             X  X  X  X  XXX        XXX  XX",
"X XXXXXX XXXXXX XXXXXXXXX    XX XX   XXXXXXXXXX  XX",
"X X    X    XXX X     XXXXXXXXX XX  XXXXXXX    X XX",
"X XXXX XXXX XXX X XXX XXX    XX    XX    XX XX X XX",
"X XXXX    X     X XXX XXX XX XXXXXXXX XX XX XX   XX",
"X      XX XXXXXXXeXXX     XX          XX    XXXXXXX",
"X               X                                 X",
"X  XXXXXXXXXX  XXXXXXXXXXXXX  XXXXXXX  XXXXXXXXXXXX",
"Xs          X                 X               XX  X",
"X  XXXXXXX  XXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX  X",
"X  X     X  X           X  X                 XXX  X",
"X  X  X  X  X  X  XXXX  X  X  XXXXXXXXXXXXX  XXX  X",
"X  X  X  X  X  X  X        X  X  X        X       X",
"X  X  XXXX  X  XXXXXXXXXX  X  X  XXXX  X  X  XX   X",
"X  X     X  X          X   X           X  X  XX  XX",
"X  XXXX  X  XXXXXXX XXXXXXXX  XXXXXXXXXXXXX  XX  XX",
"X     X  X     X              X              XX   X",
"XXXX  X  XXXXXXXXXX XXXXXXXXXXX  XXXXXXXXXX  XXX  X",
"X  X  X                    X     X     X  X  XXX  X",
"X  X  XXXX  XXXXXXXXXXXXX  X  XXXX  X  X  X  XX   X",
"X  X  X     X     X     X  X  X     X     X  XX  XX",
"X  X  X  XXXXXXX  XXXX  X  X  X  XXXXXXXXXX  XX  XX",
"X                       X  X  X              XX  XX",
"X XXXXXX             X  X  X  X  XXX        XXX  XX",
"X XXXXXX XXXXXX XXXXXXXXX    XX XX   XXXXXXXXXX  XX",
"X X    X    XXX X     XXXXXXXXX XX  XXXXXXX    X XX",
"X XXXX XXXX XXX X XXX XXX    XX    XX    XX XX X XX",
"X XXXX    X     X XXX XXX XX XXXXXXXX XX XX XX   XX",
"X      XX XXXXXXXeXXX     XX          XX    XXXXXXX",
"X               X                                 X",
"X  XXXXXXXXXX  XXXXXXXXXXXXX  XXXXXXX  XXXXXXXXXXXX",
"Xs          X                 X               XX  X",
"X  XXXXXXX  XXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX  X",
"X  X     X  X           X  X                 XXX  X",
"X  X  X  X  X  X  XXXX  X  X  XXXXXXXXXXXXX  XXX  X",
"X  X  X  X  X  X  X        X  X  X        X       X",
"X  X  XXXX  X  XXXXXXXXXX  X  X  XXXX  X  X  XX   X",
"X  X     X  X          X   X           X  X  XX  XX",
"X  XXXX  X  XXXXXXX XXXXXXXX  XXXXXXXXXXXXX  XX  XX",
"X     X  X     X              X              XX   X",
"XXXX  X  XXXXXXXXXX XXXXXXXXXXX  XXXXXXXXXX  XXX  X",
"X  X  X                    X     X     X  X  XXX  X",
"X  X  XXXX  XXXXXXXXXXXXX  X  XXXX  X  X  X  XX   X",
"X  X  X     X     X     X  X  X     X     X  XX  XX",
"X  X  X  XXXXXXX  XXXX  X  X  X  XXXXXXXXXX  XX  XX",
"X                       X  X  X              XX  XX",
"X XXXXXX             X  X  X  X  XXX        XXX  XX",
"X XXXXXX XXXXXX XXXXXXXXX    XX XX   XXXXXXXXXX  XX",
"X X    X    XXX X     XXXXXXXXX XX  XXXXXXX    X XX",
"X XXXX XXXX XXX X XXX XXX    XX    XX    XX XX X XX",
"X XXXX    X     X XXX XXX XX XXXXXXXX XX XX XX   XX",
"X      XX XXXXXXXeXXX     XX          XX    XXXXXXX",
"X               X                                 X",
"X  XXXXXXXXXX  XXXXXXXXXXXXX  XXXXXXX  XXXXXXXXXXXX",
"Xs          X                 X               XX  X",
"X  XXXXXXX  XXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX  X",
"X  X     X  X           X  X                 XXX  X",
"X  X  X  X  X  X  XXXX  X  X  XXXXXXXXXXXXX  XXX  X",
"X  X  X  X  X  X  X        X  X  X        X       X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 ]


start = 0
negative_coord = []
block_size = 7.84

# creating full range of x
for i in range(26):
    negative_coord.append(start)
    start -= block_size

positive_coord = [abs(num) for num in negative_coord]
full_range = set(positive_coord + negative_coord)
full_x_range =  ["{:.2f}".format(num) for num in sorted(list(full_range))]
full_x_range = [float(n) for n in full_x_range]

# creating full range of y
start = 0
for i in range(51):
    negative_coord.append(start)
    start -= block_size

positive_coord = [abs(num) for num in negative_coord]
full_range = set(positive_coord + negative_coord)
full_y_range =  ["{:.2f}".format(num) for num in sorted(list(full_range))]
full_y_range = sorted([float(n) for n in full_y_range], reverse=True)

grid_coord = []
for row in full_y_range:
    current_row = []
    for column in full_x_range:
        current_row.append((column, row))
    grid_coord.append(current_row)

# print(len(grid))
# print(grid_coord)

list_of_obstacle_coordinates = []
list_of_open_path_coordinates = []


# get coordinates of all obstacle blocks and open grid blocks
# loop through our rows
for i in range(101):
    # loop through each character in a row
    for k in range(51):
        if grid[i][k] == "X":
            list_of_obstacle_coordinates.append(grid_coord[i][k])
        elif grid[i][k] == " ":
            list_of_open_path_coordinates.append(grid_coord[i][k])


def get_obstacles():
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            new_x = 8 * x - 200
            new_y = -8 * y + 392
            maze_points.append((new_x, new_y))
            
            if grid[y][x] == "X":
                position_obstacles.append((new_x, new_y))

    return position_obstacles, maze_points




