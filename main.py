import turtle
from turtle import Turtle, Screen
import colorgram
import random

tim = Turtle()
screen = Screen()
turtle.colormode(255)
colors = colorgram.extract("image.jpg", 15)
tim.speed(10)
screen.bgcolor("grey")

tim.penup()
tim.setpos(-250, -250)
tim.pendown()

x_postion = -275
y_position = -250
for row in range(15):
	tim.penup()
	tim.setpos(x_postion, y_position)
	tim.pendown()
	for color in range(15):
		rand_color = random.randint(0,14)
		tim.dot(15, colors[rand_color].rgb)
		tim.penup()
		tim.forward(40)
		tim.pendown()
	y_position += 40








screen.exitonclick()
