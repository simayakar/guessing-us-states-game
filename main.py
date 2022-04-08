import turtle
import pandas
FONT_SIZE = 10
FONT = ("Arial", FONT_SIZE, "bold")

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()


text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.color("black")


score = 0
title = "Guess the State"
correct_guesses = []
states_to_learn = []

while len(correct_guesses) < 50:
    answer = screen.textinput(title=title, prompt="What's another state's name?")
    answer = answer.title()

    if answer == "Exit":
        for state in states:
            if state not in correct_guesses:
                states_to_learn.append(state)

        df = pandas.DataFrame(states_to_learn)
        df.to_csv("states_to_learn.csv")
        break

    if answer in states:
        state_x = data[data.state == answer]["x"]
        state_y = data[data.state == answer]["y"]
        text_turtle.setposition(int(state_x), int(state_y))
        text_turtle.write(answer, align="center", font=FONT)
        correct_guesses.append(answer)
        score += 1
        title = f"{score}/50 Correct"
