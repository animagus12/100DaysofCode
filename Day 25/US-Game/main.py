import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
img = "Python/#100DaysOfCode/Day 25/US-Game/blank_states_img.gif"
turtle.addshape(img)
turtle.shape(img)

data = pandas.read_csv("Python/#100DaysOfCode/Day 25/US-Game/50_States.csv")
all_state_list = data.state.to_list()
guessed_state = []
game_is_on = True
while len(guessed_state) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_state)}/{len(data.state)} Guess the State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        to_learn_list = [state for state in all_state_list if state not in guessed_state]
        new_data = pandas.DataFrame(to_learn_list)
        new_data.to_csv("Python/#100DaysOfCode/Day 25/US-Game/states_to_learn.csv")
        break

    if answer_state in all_state_list:
        guessed_state.append(answer_state)

        sam = turtle.Turtle()
        sam.hideturtle()
        sam.penup()
        state_data = data[data.state == answer_state]
        sam.goto(int(state_data.x), int(state_data.y))
        sam.write(answer_state)
