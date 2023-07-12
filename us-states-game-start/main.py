import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
guessed_states = []


while len(guessed_states) < 50:
    guess = screen.textinput(title=f"{len(guessed_states)}/ 50 states correct",
                                prompt='what\'s your next guess?').title()

    if guess == "Exit":
        missing_states = []
        for states in states_list:
            if states not in guessed_states:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if guess in states_list:
        guessed_states.append(guess)
        jimmy = turtle.Turtle()
        jimmy.hideturtle()
        jimmy.penup()
        state_data = data[data.state == guess]
        jimmy.goto(int(state_data.x), int(state_data.y))
        jimmy.write(guess)

