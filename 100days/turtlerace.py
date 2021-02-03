from turtle import Turtle, Screen
import random as r

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race: ")
colors = ["red", "blue", "orange", "green", "yellow", "black"]
tur_pos = [-70, -40, -10, 20, 50, 80]
all_tur = []

if user_bet:
    is_race_on = True

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=tur_pos[i])
    all_tur.append(new_turtle)

while is_race_on:
    for i in all_tur:
        if i.xcor() > 230:
            is_race_on = False
            winning_tur = i.pencolor()
            if winning_tur == user_bet:
                print(f"You've Won. The {winning_tur} turtle is the winner")
            else:
                print(f"You've lost. The {winning_tur} turtle is the winner")
        random_dis = r.randint(0, 10)
        i.forward(random_dis)

screen.exitonclick()
