from turtle import *
import math

# Name your Turtle.
t = Turtle()
Timmy=Turtle()
# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
### Write your code below:

sides = int(input("How many sides?"))
t.speed(50)
t.fillcolor("yellow")
t.pencolor("blue")
t.begin_fill()
for x in range(sides):
    t.forward(100)
    t.right(360/sides)
t.end_fill()

# Close window on click.
exitonclick()
