import turtle
import pandas

screen = turtle.Screen()
screen.title("American States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
print(type(data))
states = data.state.to_list()
print(states)
guesses = []

while len(guesses) < 50:

    answer = screen.textinput(f"States Guessed: {len(guesses)}", "Write another state's name.").title()
    print(answer)


    if answer in states:
        guesses.append(answer)
        tur = turtle.Turtle()
        tur.color("Black")
        tur.hideturtle()
        tur.penup()
        state_data = data[data.state == answer]
        tur.goto(float(state_data.x), float(state_data.y))
        tur.write(answer)

    if answer == "Exit":
        missed = []
        for state in states:
            if state not in guesses:
                missed.append(state)
        new_data = pandas.DataFrame(missed)
        new_data.to_csv("states_missed.csv")
        print(missed)
        break