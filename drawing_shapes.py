import turtle as t
from turtle import Screen

tim = t.Turtle()
screen = Screen()

########### Challenge 3 - Draw Shapes ########


shape_num = 3
colors = ["red", "blue", "purple", "pink", "yellow", "orange", "green", "black"]
for move in range(8):
  for shape in range(shape_num):
    tim.pencolor(colors[move])
    tim.right(360 / shape_num)
    tim.forward(100)
  shape_num += 1

screen.exitonclick()
