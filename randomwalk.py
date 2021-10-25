import turtle as t
from turtle import Screen
import random

direction = [0, 90, 180, 270, 360]
right_or_left = random.randint(1,2)

def random_color():
	r = random.randint(0,255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	color_tuple = (r, g, b)
	return color_tuple

t.colormode(255)
tim = t.Turtle()
screen = Screen()
tim.width(10)
tim.speed("fastest")

print(t.window_width())
print(t.window_height())

while True:
	random_direction = direction[random.randint(0,4)]
	right_or_left = random.randint(1, 2)
	tim.pencolor(random_color())
	if right_or_left == 1:
		tim.right(random_direction)
	else:
		tim.left(random_direction)
	tim.forward(25)
	if tim.xcor() > 480 or tim.xcor() < -480:
		tim.penup()
		tim.goto(0, 0)
		tim.pendown()
	if tim.ycor() > 405 or tim.ycor() < -405:
		tim.penup()
		tim.goto(0, 0)
		tim.pendown()


