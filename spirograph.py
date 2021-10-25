import turtle
from turtle import Screen
import random

tim = turtle
screen = Screen()
turtle.colormode(255)
tim.speed(10)

def random_color():
	r = random.randint(0,255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	color_tuple = (r, g, b)
	return color_tuple

angle = 4
stop = 360
start = 0
while start < stop / angle:
	start += 1
	tim.pencolor(random_color())
	tim.circle(100)
	tim.left(angle)


screen.exitonclick()


