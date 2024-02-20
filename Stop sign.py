#cs175
#CS175
#Ziv Cohen
#stop sign

import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

# Size the window.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
s = LENGTH
x = s / (2**0.5)
diameter = s + (2 * x)
turtle.penup()
turtle.goto(-25,80)
turtle.pendown()
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(1,NUM_SIDES+1):
    turtle.forward(100)
    turtle.right(45)
turtle.end_fill()
turtle.penup()
turtle.goto(-20,65)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
for i in range(1,NUM_SIDES+1):
    turtle.forward(90)
    turtle.right(45)
turtle.end_fill()
turtle.penup()
turtle.goto(-15,50)
turtle.pendown()
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(1,NUM_SIDES+1):
    turtle.forward(80)
    turtle.right(45)
turtle.end_fill()
turtle.penup()
turtle.goto(30,-75)
turtle.pendown()
turtle.color('white')
turtle.hideturtle()
turtle.write("STOP", align="center", font=("Times New Roman",38, "normal"))
 
turtle.done()

    
