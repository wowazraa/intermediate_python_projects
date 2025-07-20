from turtle import *
import pandas

screen = Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

map_america = Turtle()
map_america.shape(image)

state = Turtle()
state.penup()
state.hideturtle()

data = pandas.read_csv("50_states.csv")
correct_guess = 0
guessed_states = []

while correct_guess < 50:
    answer_state = screen.textinput(
        title=f"{correct_guess}/50 States Correct",
        prompt="What's another state's name?"
    )

    if answer_state.lower() == "exit" or answer_state is None:
        missing_states = [state for state in data["state"] if state not in guessed_states]
        unguessed = pandas.DataFrame(missing_states)
        unguessed.to_csv("states_to_learn.csv")
        break

    for state_name in data["state"]:
        if state_name.lower() == answer_state.lower() and state_name.title() not in guessed_states:
            x = int(data[data.state == state_name]["x"].iloc[0])
            y = int(data[data.state == state_name]["y"].iloc[0])
            state.goto(x, y)
            state.write(f"{state_name}")
            correct_guess += 1
            guessed_states.append(state_name)

