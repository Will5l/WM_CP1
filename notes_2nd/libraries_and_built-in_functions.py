# WM 2nd Libraries notes
import random
import turtle
number = random.randint(100,500)
turtle.shape("turtle")
turtle.shapesize(150)
turtle.color("#144DC9")
turtle.pensize(20)
turtle.fillcolor("#0F915B")
turtle.begin_fill()
for x in range(4):
    turtle.forward(250)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(-500, 10)
turtle.pendown()
turtle.begin_fill()
for x in range(4):
    turtle.forward(250)
    turtle.right(90)
turtle.end_fill()
turtle.done()