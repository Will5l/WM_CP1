# WM 2nd Turtle Race
import random
import turtle
#set variables for screen and wins
screen = turtle.Screen()
screen.setup(2500, 1250)
red_win = False
yellow_win = False
blue_win = False
green_win = False
purple_win = False
game_done = False
#set prog and turtle variables
red_prog = 0
yellow_prog = 0
blue_prog = 0
green_prog = 0
purple_prog = 0
movement = 0
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()
turtle4 = turtle.Turtle()
turtle5 = turtle.Turtle()
finish_line = turtle.Turtle()
#Set shapes and colors
turtle1.penup()
turtle2.penup()
turtle3.penup()
turtle4.penup()
turtle5.penup()
turtle1.shape("turtle")
turtle2.shape("turtle")
turtle3.shape("turtle")
turtle4.shape("turtle")
turtle5.shape("turtle")
turtle1.color("#810808")
turtle2.color("#DDDA13")
turtle3.color("#1A8A99")
turtle4.color("#14C974")
turtle5.color("#6713C7")
turtle1.shapesize(4)
turtle2.shapesize(4)
turtle3.shapesize(4)
turtle4.shapesize(4)
turtle5.shapesize(4)
#make finish line
finish_line.hideturtle()
finish_line.penup()
finish_line.sety(600)
finish_line.color("black")
finish_line.pensize(5)
finish_line.pendown()
finish_line.sety(-600)
#put turtles in positions
turtle1.setposition(-1000, 400)
turtle2.setposition(-1000, 200)
turtle3.setposition(-1000, 0)
turtle4.setposition(-1000, -200)
turtle5.setposition(-1000, -400)
turtle1.pendown()
turtle2.pendown()
turtle3.pendown()
turtle4.pendown()
turtle5.pendown()
#Actual game loop
while True:
    movement = random.randint(1,50)
    turtle1.forward(movement)
    red_prog += movement
    movement = random.randint(1,50)
    turtle2.forward(movement)
    yellow_prog += movement
    movement = random.randint(1,50)
    turtle3.forward(movement)
    blue_prog += movement
    movement = random.randint(1,50)
    turtle4.forward(movement)
    green_prog += movement
    movement = random.randint(1,50)
    turtle5.forward(movement)
    purple_prog += movement
    #Win conditions
    if red_prog >= 1000:
        red_win = True
        break
    elif yellow_prog >= 1000:
        yellow_win = True
        break
    elif blue_prog >= 1000:
        blue_win = True
        break
    elif green_prog >= 1000:
        green_win = True
        break
    elif purple_prog >= 1000:
        purple_win = True
        break
#Display winner
if red_win == True:
    print("Red Won")
elif yellow_win == True:
    print("Yellow Won")
elif blue_win == True:
    print("Blue Won")
elif green_win == True:
    print("Green Won")
elif purple_win == True:
    print("Purple Won")
