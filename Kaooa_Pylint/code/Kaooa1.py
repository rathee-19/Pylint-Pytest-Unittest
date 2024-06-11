import turtle
import math

Divya = turtle.Screen()
Divya.bgcolor("lightgreen")


vulture = turtle.Turtle()
vulture.color("blue")
vulture.shape("circle")
vulture.penup()
vulture.setposition(-377,-17)
# vulture.speed(0)

speed = 2
star = turtle.Turtle()
# star.color("black")
# star.shape("triangle")
star.penup()
star.setposition(-350,150)
star.pendown()
star.pensize(3)
star.speed(70)

def createCrow(x, y):
    crow = turtle.Turtle()
    crow.penup()
    crow.speed(100)
    crow.setposition(x, y)
    crow.color("yellow")
    crow.shape("circle")
    return crow

# Define positions for the crows
positions = [(500, 0), (500, 100), (500, -100), (500, 200), (500, -200), (500, 300), (500, -300)]

# Create crows using a for loop
crows = []
for position in positions:
    crow = createCrow(position[0], position[1])
    crows.append(crow)

# Example usage: Accessing one of the crows
# crows[0].forward(100)  # Move the first crow forward by 100 units

# star_points  = []
def get_click_coord(x,y):
    print(f"Clicked at: ({x}, {y})")
    d = math.sqrt(math.pow(x,))

clicked_points = [(-2.0, -103.0), (-213.0, -261.0), (218.0, -263.0), (133.0, -10.0),
                  (-132.0, -9.0), (-79.0, 153.0), (84.0, 148.0), (0.0, 403.0),
                  (-347.0, 148.0), (347,148)]
valid_list = [    [1, 2, 3, 4],  # Valid moves for point 1 (-2.0, -103.0)
    [4, 0],  # Valid moves for point 2 (-213.0, -261.0)
    [0, 3],  # Valid moves for point 3 (218.0, -263.0)
    [0, 2 , 6, 9],  # Valid moves for point 4 (133.0, -10.0)
    [1, 0, 5, 8],  # Valid moves for point 6 (-79.0, 153.0)
    [4, 6, 8, 7],  # Valid moves for point 5 (-132.0, -9.0)
    [3, 5, 7, 9],  # Valid moves for point 7 (84.0, 148.0)
    [5, 6],  # Valid moves for point 8 (0.0, 403.0)
    [5, 4],  # Valid moves for point 9 (-347.0, 148.0)
    [6, 3]  # Valid moves for point 10 (347, 148)
]
valid_kill =[
[8,9],
[3,5],
[4,6],
[1,7],
[2,7],
[9,1],
[2,8],
[3,4],
[0,6],
[5,0]
]
Is_present =[0,0,0,0,0,0,0,0,0,0]

def get_distance(point1, point2):
    """Calculate distance between two points"""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

flag =0
def check_click(x, y):
    turtle.onscreenclick(None)
    """Check if click is within a radius of 20 of any of the clicked points"""
    global flag
    global num
    global killed

    for point in clicked_points:
        # print(point)
        distance = get_distance((x, y), point)
        if distance <= 60:
            print(f"Clicked near point: {point}")
            t1 = point[0]
            t2 = point[1]
            # check_crow(t1,t2)

            if Is_present[clicked_points.index(point)] ==0 and turn == 1:
                if crows[pos].xcor()!=500:
                   Is_present[clicked_points.index((crows[pos].xcor(),crows[pos].ycor()))] =0
                   index =clicked_points.index((crows[pos].xcor(),crows[pos].ycor()))  # Get index of the position in clicked_points
                   if clicked_points.index(point) in valid_list[index]:
                     turtle.penup()
                     crows[pos].goto(t1,t2)
                     num = num +1
                     turtle.pendown()
                     # print(flag)
                     flag = flag +1
                     Is_present[clicked_points.index(point)]=1
                     if(vulture.xcor() != -377):
                         crows_winner()
                     
                #    elif clicked_points.index(point)  in valid_kill[index] and Is_present[cli]
                   else:
                       print("Invalid move")
                       break
                elif crows[pos].xcor() ==500 :

                     turtle.penup()
                     crows[pos].goto(t1,t2)
                     num = num +1
                     turtle.pendown()
                     # print(flag)
                     flag = flag +1
                     Is_present[clicked_points.index(point)]=1
                     if(vulture.xcor() != -377):
                         crows_winner()
            elif Is_present[clicked_points.index(point)] ==0  and turn ==2:
                print("coming here or ?")
                if vulture.xcor()!=-377:
                   index =clicked_points.index((vulture.xcor(),vulture.ycor()))  # Get index of the position in clicked_points
                   if clicked_points.index(point) in valid_list[index] :
                      Is_present[clicked_points.index((vulture.xcor(),vulture.ycor()))] =0
                      
                      print(Is_present)
                      turtle.penup()
                      vulture.goto(t1,t2)
                      num = num +1
                      turtle.pendown()
                      Is_present[clicked_points.index(point)]=1
                   elif  clicked_points.index(point) in   valid_kill[index] and Is_present[clicked_points.index(point)] ==0:
                        common = valid_kill[index]
                        for z in common:
                         
                            for y in valid_list[z]:
                              
                                if y in valid_list[index] and Is_present[y] == 1 and z== clicked_points.index(point):
                                    print("present arrray",Is_present[y])
                                    
                                    print("y",y)
                                    print("killed")
                                    killed = killed+1
                                    if killed>3:
                                        print("vulture winner")
                                        exit()
                                    Is_present[index] = 0
                                    Is_present[y] = 0
                                    turtle.penup()
                                    vulture.goto(t1,t2)
                                    
                                    num = num +1
                                    turtle.pendown()
                                    killx = clicked_points[y][0]
                                    killy = clicked_points[y][1]
                                    for i in range(7):
                                        if crows[i].xcor() == killx and crows[i].ycor()==killy:
                                            crows[i].goto(700,800)
                                    Is_present[clicked_points.index(point)]=1
                                    
                                else:
                                    print("wrong try to kill")   
                                    # break
                   else:
                       print("Invalid move")
                       break
                elif vulture.xcor() == -377:

                 turtle.penup()
                 vulture.goto(t1,t2)
                 num = num +1
                 turtle.pendown()
                 Is_present[clicked_points.index(point)]=1
    # turtle.onscreenclick(check_click_vulture)
    # turtle.onscreenclick(check_click_crow)
    if num%2==0:
        # print(num)
        turtle.onscreenclick(check_click_crow)
    else:    
     turtle.onscreenclick(check_click_vulture)    
def crows_winner(): 
    print("I came here")
    crowcount = 0
    crowcount2 = 0
    for i in valid_list[clicked_points.index((vulture.xcor(),vulture.ycor()))]:
        if Is_present[i] == 1:
            crowcount += 1
    for i in valid_kill[clicked_points.index((vulture.xcor(),vulture.ycor()))]:
        if Is_present[i] == 1:
            crowcount2 += 1
    if(crowcount == 2 and clicked_points.index((vulture.xcor(),vulture.ycor())) in [1,2,7,8,9] and crowcount2 == 2):
        print("Crows win")
        exit()
    elif(crowcount == 4 and clicked_points.index((vulture.xcor(),vulture.ycor())) in [0,3,4,5,6] and crowcount2 == 2):
        print("Crows win")
        exit()
    else:
        turtle.onscreenclick(check_click_crow)   
def check_click_crow(x, y):
      global pos
      global turn
      turn =1
      for point in crows:
        dummypoint = (point.xcor(),point.ycor())
        distance = get_distance((x, y), dummypoint)
        if distance <= 60:
            print(f"Clicked near point: {point}")
            # t1,t2 = point
            # check_crow(t1,t2)
            # print(flag)
            # flag = flag +1
            pos = crows.index(point)
            print(pos)
            turtle.onscreenclick(check_click)


def check_click_vulture(x, y):
    #   global pos
        global turn 
        turn =2 
        dummypoint = (vulture.xcor(),vulture.ycor())
        distance = get_distance((x, y), dummypoint)
        if distance <= 60:
            print(f"Clicked near point: {vulture.xcor(),vulture.ycor()}")
            # t1,t2 = point
            # check_crow(t1,t2)
            # print(flag)
            # flag = flag +1
            # pos = crows.index(point)
            # print(pos)
            turtle.onscreenclick(check_click)            

def check_crow(t1,t2):
    crows[0].setposition(t1,t2)
    

for size in range(5):
    star.forward(700)
 
    star.right(144)

star.hideturtle()



def turnleft():
    vulture.left(30)
    
def turnright():
    vulture.right(30)

def increaseSpeed():
    global speed
    speed=speed+0.5

def decreaseSpeed():
    global speed
    speed=speed-0.5

        
#keyboard binding
turtle.listen () # it will listen for keyboard inputs
turtle.onkey(turnleft, "Left" )
turtle.onkey(turnright, "Right" )
turtle.onkey(increaseSpeed,"Up")
turtle.onkey(decreaseSpeed,"Down")

global pos
pos = 0
global turn 
turn = 0
global num
num = 0
global killed
killed = 0
# print(crows[0].xcor(),crows[0].ycor())
turtle.onscreenclick(check_click_crow)
# turtle.onscreenclick(check_click_vulture)



delay = input("Press Enter to stop.")

# screen.bye()
