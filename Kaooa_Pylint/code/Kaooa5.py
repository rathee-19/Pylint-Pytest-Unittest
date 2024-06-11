import turtle
import math
import sys
"""
This is a Indian Board Game
"""
# Initialize screen and set background color
DIVYA = turtle.Screen()
DIVYA.bgcolor("lightgreen")

# Initialize vulture turtle
vulture = turtle.Turtle()
vulture.color("blue")
vulture.shape("circle")
vulture.penup()
vulture.setposition(-377, -17)

# Initialize star turtle
star = turtle.Turtle()
star.penup()
star.setposition(-350, 150)
star.pendown()
star.pensize(3)
star.speed(70)

# Define positions for the crows
POSITIONS = [(500, 0), (500, 100), (500, -100), (500, 200), (500, -200), (500, 300), (500, -300)]

# Create crows using a for loop
crows = [create_crow(position[0], position[1]) for position in POSITIONS]

# Define clicked points and valid movements for each point
CLICKED_POINTS = [(-2.0, -103.0), (-213.0, -261.0), (218.0, -263.0), (133.0, -10.0),
                  (-132.0, -9.0), (-79.0, 153.0), (84.0, 148.0), (0.0, 403.0),
                  (-347.0, 148.0), (347, 148)]
VALID_LIST = [[1, 2, 3, 4], [4, 0], [0, 3], [0, 2, 6, 9], [1, 0, 5, 8], [4, 6, 8, 7],
               [3, 5, 7, 9], [5, 6], [5, 4], [6, 3]]
VALID_KILL = [[8, 9], [3, 5], [4, 6], [1, 7], [2, 7], [9, 1], [2, 8], [3, 4], [0, 6], [5, 0]]
IS_PRESENT = [0] * 10

# Global variables
POS = 0
TURN = 0
NUM = 0
KILLED = 0
FLAG = 0

# Define functions
def create_crow(x, y):
    """
    This function creates crow"""
    crow = turtle.Turtle()
    crow.penup()
    crow.speed(100)
    crow.setposition(x, y)
    crow.color("yellow")
    crow.shape("circle")
    return crow

def get_distance(point1, point2):
    """this function is used to find distance between two points"""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def check_click_crow(x, y):
    """if we click i radius of 60 of the crow then the click is counted and
      check_click after that"""
    global POS
    global TURN
    TURN = 1
    for point in crows:
        distance = get_distance((x, y), (point.xcor(), point.ycor()))
        if distance <= 60:
            POS = crows.index(point)
            turtle.onscreenclick(check_click)

def check_click_vulture(x, y):
    """ similarly doing it for vulture"""
    global TURN
    TURN = 2
    distance = get_distance((x, y), (vulture.xcor(), vulture.ycor()))
    if distance <= 60:
        turtle.onscreenclick(check_click)

def check_click(x, y):
    """this functions checks click alternatively and
      main logic for the game is here checking if the position is empty or valid move or not"""
    turtle.onscreenclick(None)
    global FLAG
    global NUM
    global KILLED

    for point in CLICKED_POINTS:
        distance = get_distance((x, y), point)
        if distance <= 60:
            t1, t2 = point
            index = CLICKED_POINTS.index(point)

            if IS_PRESENT[index] == 0 and TURN == 1:
                if crows[POS].xcor() != 500:
                    IS_PRESENT[CLICKED_POINTS.index((crows[POS].xcor(), crows[POS].ycor()))] = 0
                    if CLICKED_POINTS.index(point) in VALID_LIST[index]:
                        turtle.penup()
                        crows[POS].goto(t1, t2)
                        NUM += 1
                        FLAG += 1
                        IS_PRESENT[CLICKED_POINTS.index(point)] = 1
                        if vulture.xcor() != -377:
                            crows_winner()
                    else:
                        print("Invalid move")
                        break
                elif crows[POS].xcor() == 500:
                    turtle.penup()
                    crows[POS].goto(t1, t2)
                    NUM += 1
                    FLAG += 1
                    IS_PRESENT[CLICKED_POINTS.index(point)] = 1
                    if vulture.xcor() != -377:
                        crows_winner()

            elif IS_PRESENT[index] == 0 and TURN == 2:
                if vulture.xcor() != -377:
                    index = CLICKED_POINTS.index((vulture.xcor(), vulture.ycor()))
                    if CLICKED_POINTS.index(point) in VALID_LIST[index]:
                        IS_PRESENT[CLICKED_POINTS.index((vulture.xcor(), vulture.ycor()))] = 0
                        turtle.penup()
                        vulture.goto(t1, t2)
                        NUM += 1
                        IS_PRESENT[CLICKED_POINTS.index(point)] = 1
                    elif CLICKED_POINTS.index(point) in VALID_KILL[index] and IS_PRESENT[CLICKED_POINTS.index(point)] == 0:  # pylint: disable=line-too-long
                        common = VALID_KILL[index]
                        for z in common:
                            for y in VALID_LIST[z]:
                                if y in VALID_LIST[index] and IS_PRESENT[y] == 1 and z == CLICKED_POINTS.index(point):# pylint: disable=line-too-long
                                    KILLED += 1
                                    if KILLED > 3:
                                        print("vulture winner")
                                        sys.exit()
                                    IS_PRESENT[index] = 0
                                    IS_PRESENT[y] = 0
                                    turtle.penup()
                                    vulture.goto(t1, t2)
                                    NUM += 1
                                    killx = CLICKED_POINTS[y][0]
                                    killy = CLICKED_POINTS[y][1]
                                    for i in range(7):
                                        if crows[i].xcor() == killx and crows[i].ycor() == killy:
                                            crows[i].goto(700, 800)
                                    IS_PRESENT[CLICKED_POINTS.index(point)] = 1
                                else:
                                    print("wrong try to kill")
                    else:
                        print("Invalid move")
                        break
                elif vulture.xcor() == -377:
                    turtle.penup()
                    vulture.goto(t1, t2)
                    NUM += 1
                    IS_PRESENT[CLICKED_POINTS.index(point)] = 1

    if NUM % 2 == 0:
        turtle.onscreenclick(check_click_crow)
    else:
        turtle.onscreenclick(check_click_vulture)

def crows_winner():
    """functions decides if crows are winner"""
    crowcount = 0
    crowcount2 = 0
    for i in VALID_LIST[CLICKED_POINTS.index((vulture.xcor(), vulture.ycor()))]:
        if IS_PRESENT[i] == 1:
            crowcount += 1
    for i in VALID_KILL[CLICKED_POINTS.index((vulture.xcor(), vulture.ycor()))]:
        if IS_PRESENT[i] == 1:
            crowcount2 += 1
    if (crowcount == 2 and CLICKED_POINTS.index((vulture.xcor(), vulture.ycor())) in [1, 2, 7, 8, 9] and crowcount2 == 2)  or (crowcount == 4 and CLICKED_POINTS.index((vulture.xcor(), vulture.ycor())) in [0, 3, 4, 5, 6] and crowcount2 == 2): # pylint: disable=line-too-long
        print("Crows win")
        sys.exit()
    else:
        turtle.onscreenclick(check_click_crow)

# Initial click
turtle.onscreenclick(check_click_crow)

# Exit condition
input("Press Enter to stop.")
