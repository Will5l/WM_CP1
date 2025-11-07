#WM 2nd Maze Project
import turtle
import random
#setup variables
turtle.speed(50)
grid_row = [[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),],
            [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),],
            [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),],
            [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),],
            [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),],
            [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),]]
grid_columnes = [[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),],
            [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),],
            [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),],
            [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),],
            [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),],
            [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),]]
#make function for maze setup
def mazeSetup():
    #have a turtle draw the outside walls for the maze
    turtle.penup()
    turtle.setposition(-300,-300)
    turtle.forward(100)
    turtle.pendown()
    turtle.forward(600)
    turtle.left(90)
    turtle.forward(700)
    turtle.left(90)
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.forward(600)
    turtle.left(90)
    turtle.forward(700)
    turtle.left(90)

mazeSetup()
    #set it to the first position for the drawing of the inside walls
#make function for checking if the maze is solvable
def isSolvable():
    global grid_row
    global grid_columnes
    solvable = False
    while solvable == False:

        if solvable == False:
            for u in range(0,6):
                for i in range(0,6):
                    grid_row[u][i] = (random.randint(0,1))
            for u in range(0,6):
                for i in range(0,6):
                    grid_columnes[u][i] = (random.randint(0,1))
    #have it fill the list with the numbers, and if it needs to, have it refill them.
#make function for the actual maze generation
def mazeGen():
    y = 0
    z = 0
    x = 0
    switch = False
    turtle.setposition(-300,-200)
    thing = -200
    while True:
        if z == 6 and x == 0:
            thing += 100
            z = 0
            y += 1
            turtle.forward(100)
            turtle.penup()
            turtle.setposition(-300,thing)
        if z == 6 and x == 1:
            thing += 100
            z = 0
            y += 1
            turtle.forward(100)
            turtle.penup()
            turtle.setposition(thing,-300)
        if y == 6:
            y = 0
            z = 0
            x += 1
            switch == True
            thing = -200
            turtle.left(90)
            turtle.setposition(-200,-300)
        if grid_row[y][z] == 1 and x == 0:
            turtle.pendown()
            turtle.forward(100)
            z += 1
        elif grid_row[y][z] == 0 and x == 0:
            turtle.penup()
            turtle.forward(100)
            z += 1
        elif x == 0 and switch == True:
            turtle.setposition(-200,-300)
            switch == False
        elif grid_columnes[y][z] == 1 and x == 1:
            turtle.pendown()
            turtle.forward(100)
            z += 1
        elif grid_columnes[y][z] == 0 and x == 1:
            turtle.penup()
            turtle.forward(100)
            z += 1
    
        
    #have a turtle draw the inside walls after the solvable function based on the lists, where 1 is a wall and pen goes down, and 0 is not a wall, the pen going up
mazeGen()
turtle.done