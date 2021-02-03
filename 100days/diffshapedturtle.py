from turtle import Turtle, Screen
import random

colors = ["CornflowerBlue", "IndianRed", "DeepSkyBlue", "LightSeaGreen"]

tim = Turtle()
tim.shape("turtle")


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(50)
        tim.right(angle)


for n in range(3, 10):
    tim.color(random.choice(colors))
    draw_shape(n)

screen = Screen()
screen.exitonclick()
