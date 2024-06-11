import turtle
import math

def create_crow(x, y):
    crow = turtle.Turtle()
    crow.penup()
    crow.speed(100)
    crow.setposition(x, y)
    crow.color("yellow")
    crow.shape("circle")
    return crow

def get_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def check_click_crow(x, y):
    global pos
    global turn
    turn = 1
    for point in crows:
        distance = get_distance((x, y), (point.xcor(), point.ycor()))
        if distance <= 60:
            pos = crows.index(point)
            turtle.onscreenclick(check_click)

def check_click_vulture(x, y):
    global turn
    turn = 2
    distance = get_distance((x, y), (vulture.xcor(), vulture.ycor()))
    if distance <= 60:
        turtle.onscreenclick(check_click)

def check_click(x, y):
    turtle.onscreenclick(None)
    global flag
    global num
    global killed

    for point in clicked_points:
        distance = get_distance((x, y), point)
        if distance <= 60:
            t1, t2 = point
            index = clicked_points.index(point)

            if Is_present[index] == 0 and turn == 1:
                if crows[pos].xcor() != 500:
                    Is_present[clicked_points.index((crows[pos].xcor(), crows[pos].ycor()))] = 0
                    if clicked_points.index(point) in valid_list[index]:
                        turtle.penup()
                        crows[pos].goto(t1, t2)
                        num += 1
                        flag += 1
                        Is_present[clicked_points.index(point)] = 1
                        if vulture.xcor() != -377:
                            crows_winner()
                    else:
                        print("Invalid move")
                        break
                elif crows[pos].xcor() == 500:
                    turtle.penup()
                    crows[pos].goto(t1, t2)
                    num += 1
                    flag += 1
                    Is_present[clicked_points.index(point)] = 1
                    if vulture.xcor() != -377:
                        crows_winner()

            elif Is_present[index] == 0 and turn == 2:
                if vulture.xcor() != -377:
                    index = clicked_points.index((vulture.xcor(), vulture.ycor()))
                    if clicked_points.index(point) in valid_list[index]:
                        Is_present[clicked_points.index((vulture.xcor(), vulture.ycor()))] = 0
                        turtle.penup()
                        vulture.goto(t1, t2)
                        num += 1
                        Is_present[clicked_points.index(point)] = 1
                    elif clicked_points.index(point) in valid_kill[index] and Is_present[clicked_points.index(point)] == 0:
                        common = valid_kill[index]
                        for z in common:
                            for y in valid_list[z]:
                                if y in valid_list[index] and Is_present[y] == 1 and z == clicked_points.index(point):
                                    killed += 1
                                    if killed > 3:
                                        print("vulture winner")
                                        exit()
                                    Is_present[index] = 0
                                    Is_present[y] = 0
                                    turtle.penup()
                                    vulture.goto(t1, t2)
                                    num += 1
                                    killx = clicked_points[y][0]
                                    killy = clicked_points[y][1]
                                    for i in range(7):
                                        if crows[i].xcor() == killx and crows[i].ycor() == killy:
                                            crows[i].goto(700, 800)
                                    Is_present[clicked_points.index(point)] = 1
                                else:
                                    print("wrong try to kill")
                    else:
                        print("Invalid move")
                        break
                elif vulture.xcor() == -377:
                    turtle.penup()
                    vulture.goto(t1, t2)
                    num += 1
                    Is_present[clicked_points.index(point)] = 1

    if num % 2 == 0:
        turtle.onscreenclick(check_click_crow)
    else:
        turtle.onscreenclick(check_click_vulture)

def crows_winner():
    crowcount = 0
    crowcount2 = 0
    for i in valid_list[clicked_points.index((vulture.xcor(), vulture.ycor()))]:
        if Is_present[i] == 1:
            crowcount += 1
    for i in valid_kill[clicked_points.index((vulture.xcor(), vulture.ycor()))]:
        if Is_present[i] == 1:
            crowcount2 += 1
    if (crowcount == 2 and clicked_points.index((vulture.xcor(), vulture.ycor())) in [1, 2, 7, 8, 9] and crowcount2 == 2) \
            or (crowcount == 4 and clicked_points.index((vulture.xcor(), vulture.ycor())) in [0, 3, 4, 5, 6] and crowcount2 == 2):
        print("Crows win")
        exit()
    else:
        turtle.onscreenclick(check_click_crow)

# Initialize screen and set background color
Divya = turtle.Screen()
Divya.bgcolor("lightgreen")

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
positions = [(500, 0), (500, 100), (500, -100), (500, 200), (500, -200), (500, 300), (500, -300)]

# Create crows using a for loop
crows = [create_crow(position[0], position[1]) for position in positions]

# Define clicked points and valid movements for each point
clicked_points = [(-2.0, -103.0), (-213.0, -261.0), (218.0, -263.0), (133.0, -10.0),
                  (-132.0, -9.0), (-79.0, 153.0), (84.0, 148.0), (0.0, 403.0),
                  (-347.0, 148.0), (347, 148)]
valid_list = [[1, 2, 3, 4], [4, 0], [0, 3], [0, 2, 6, 9], [1, 0, 5, 8], [4, 6, 8, 7], [3, 5, 7, 9], [5, 6], [5, 4], [6, 3]]
valid_kill = [[8, 9], [3, 5], [4, 6], [1, 7], [2, 7], [9, 1], [2, 8], [3, 4], [0, 6], [5, 0]]
Is_present = [0] * 10

# Global variables
pos = 0
turn = 0
num = 0
killed = 0
flag = 0

# Drawing star
for _ in range(5):
    star.forward(700)
    star.right(144)
star.hideturtle()

# Keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increaseSpeed, "Up")
turtle.onkey(decreaseSpeed, "Down")

# Initial click
turtle.onscreenclick(check_click_crow)

# Exit condition
delay = input("Press Enter to stop.")
