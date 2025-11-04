#WM 2nd Maze Project
import turtle
import random
global grid_columnes
global grid_rows
#gen maze function
grid_rows = []
grid_columnes = []
def mazeGen():
    global grid_columnes
    global grid_rows
    while True:
        turtle.penup()
        turtle.setposition(-200,-200)
        turtle.pendown()
        turtle.forward(400)
        turtle.left(90)
        turtle.forward(400)
        turtle.left(90)
        turtle.forward(400)
        turtle.left(90)
        turtle.forward(400)
        turtle.left(90)
        turtle.penup()
        turtle.setposition(-150,-150)
        for x in grid_rows:
            if x == 1:
                turtle.pendown()
                turtle.forward(50)
            if x == 0:
                turtle.penup()
                turtle.forward(50)
#check if solvable function
def isSolvable(grid_rows, grid_columnes):
    size = len(grid_rows)
    visited = set()
    stack = [(0,0)]

    while stack:
        x, y = stack.pop()

        if x == size - 1 and y ==  size - 1:
            return True
        
        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x < size - 1 and grid_columnes[y][x+1] == 0:
            stack.append((x+1, y))
        
        if y < size - 1 and grid_rows[y+1][x] == 0:
            stack.append((x, y+1))
        
        if x > 0 and grid_columnes[y][x] == 0:
            stack.append((x-1, y))
        
        if y > 0 and grid_rows[y][x] == 0:
            stack.append((x, y-1))
    return False
while isSolvable == False:
    grid_rows = [[random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2)]
             [random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2)]
             [random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2)]
             [random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2)]
             [random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2)]
             [random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2)]]
    grid_columnes = [[random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2)]  
                 [random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2)]
                 [random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2)]
                 [random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2)]
                 [random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2)]
                 [random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2)]]
    mazeGen()
    isSolvable(grid_rows, grid_columnes)
mazeGen()
turtle.done()