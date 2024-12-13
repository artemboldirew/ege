from turtle import *
tracer(0)
r = 10
left(90)
screensize(3000, 2000)
for i in range(9):
    forward(22 * r)
    right(90)
    forward(6 * r)
    right(90)
up()
forward(1 * r)
right(90)
forward(5 * r)
left(90)
down()
for i in range(9):
    forward(53 * r)
    right(90)
    forward(75 * r)
    right(90)
up()
for x in range(-350, 10):
    for y in range(-40, 30):
        goto(x * r, y * r)
        dot(2, "red")
exitonclick()