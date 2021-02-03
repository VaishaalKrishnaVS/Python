from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")

for i in range(50):
    if i % 2 == 0:
        tim.pd()
        tim.forward(2)
    else:
        tim.pu()
        tim.forward(2)


screen = Screen()
screen.exitonclick()
