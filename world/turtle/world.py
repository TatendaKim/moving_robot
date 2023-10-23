import turtle
from maze.simple_maze import *

# from robot import my_maze #maze_list
import maze.obstacles as obstacles
import maze.simple_maze as maze
# from robot import list as obstacle_list


turtle.title("My Turtle Toy Robot")
screen = turtle.getscreen()  # Creating turtle screen
turtle.lt(90)
turtle.pencolor("black")
turtle.shape(name="turtle")
screen.bgcolor("white")
screen.setworldcoordinates

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -400, 400
min_x, max_x = -200, 200

# if my_maze == "obstacles":
# Draw boarder
turtle_position = turtle.pos()

def draw_border():
    turtle.tracer(False)
    turtle.penup()
    turtle.goto(max_x,max_y)
    turtle.pendown()
    turtle.goto(max_x,min_y)
    turtle.goto(min_x,min_y)
    turtle.goto(min_x,max_y)
    turtle.goto(max_x,max_y)
    turtle.penup()
    turtle.goto(turtle_position)
    turtle.tracer(True)

    # change turtle heading to north
    turtle.setheading(90)


def show_position(robot_name):
    turtle.goto(position_x,position_y)
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def is_position_allowed_m(new_x, new_y):
    list_of_obstacles = maze.list_of_obstacle_coordinates
    formatted_list = []
    for coord in list_of_obstacles:
        x, y = coord
        x, y = int(x), int(y)
        formatted_list.append((x, y))
    x_obs = []
    
    y_obs = []
    for x, y in formatted_list:
        x, y = int(x), int(y)
        if new_x == x and new_y == y:
            x_obs.append(True)
        # elif new_y == y:
        #     y_obs.append(True)
    if True in x_obs or True in y_obs:
        return False
    else:
        return True


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps
    
    if is_position_allowed(new_x, new_y) and not obstacles.is_path_blocked(position_x, position_y, new_x, new_y, maze_list):
        
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        turtle.fd(steps)
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        turtle.bk(-steps)
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    turtle.rt(90)
    
    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    turtle.lt(90)
    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'

def show_obstacles(position_obstacles):
    """_These function draws the obstacles_
    """
    turtle.tracer(False)
    for i in position_obstacles:
        turtle.penup()
        turtle.goto(i[0],i[1])
        turtle.pendown()
        turtle.begin_fill()
        turtle.goto(i[0],i[1])
        turtle.goto(i[0] + 4, i[1])
        turtle.goto(i[0] + 4, i[1] + 4)
        turtle.goto(i[0], i[1] + 4)
        turtle.goto(i[0], i[1])
        turtle.end_fill()
        turtle.up()
        # turtle.hideturtle()

    turtle.home()
    turtle.tracer(True)
    turtle.color("red")

    #here i am increasing the size of my turtle
    size = turtle.turtlesize()
    increase = tuple([0.6 * num for num in size])
    turtle.turtlesize(*increase) #this is where the error occurs


    # change turtle heading to north
    turtle.setheading(90)

# else:
#     setup_maze(grid)
    # wn.exitonclick()   
def setup_nodes(coordinates):
    """This function finds the neighboring obstacle for each point"""
    node = {key : [] for key in coordinates}
    for ob in node.keys():
        x, y = ob
        if (x + 8, y) in coordinates:
            node[ob].append((x + 8, y))
        if (x - 8, y) in coordinates:
            node[ob].append((x - 8, y))
        if (x, y + 8) in coordinates:
            node[ob].append((x , y + 8))
        if (x + 8, y) in coordinates:
            node[ob].append((x, y - 8))

    return node


def bfs(nodes, start, stop, obstacles):
    """This function checks for every possible path"""
    queue = [start]
    visited = [start]
    path = {}
    while len(queue) > 0:
        current = queue.pop(0)
        if current == stop:
            return path
        for block in nodes[current]:
            if block not in visited and block not in obstacles:
                visited.append(block)
                queue.append(block)
                path[block] = current

    return path


def shortest_route(path, start, stop):
    """This function takes the shortest path"""
    route = [stop]
    position = stop
    while position != start:
        position = path[position]
        route.append(position)
    
    #route is reversed
    return route

def reverse(route):
    new = route[::-1]