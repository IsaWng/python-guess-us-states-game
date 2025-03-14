import turtle
from turtle import Turtle

import pandas as pd

TOTAL = 50

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

turtle = Turtle()
turtle.penup()
turtle.hideturtle()

data = pd.read_csv("50_states.csv")
answered_states = []
state_list = data["state"].tolist()
missed_states = []
while len(answered_states) < TOTAL:
    answer_state = screen.textinput(title=f"{len(answered_states)}/50 States Correct",
                                    prompt="What's another state's name?").strip().title()
    if answer_state == "Exit":
        missed_states = [item for item in state_list if item not in answered_states]
        pd.DataFrame(missed_states).to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        location = data.loc[data["state"] == answer_state]
        x = location.x.item()
        y = location.y.item()
        turtle.goto(x, y)
        turtle.write(answer_state)
        answered_states.append(answer_state)

screen.exitonclick()
