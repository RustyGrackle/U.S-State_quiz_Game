import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image) # added to screen now available to turtle to use it
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # answer_state contains whatever I write in that question box
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv") # states to learn.csv
        break

    #Check if the guess is among 50 states
    if answer_state in all_states:
        guessed_states.append(answer_state)
        #Create a turtle to write name of the state at the state's x and y
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] #row of a data.. and hence we can call by name of columns as below:
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)



screen.exitonclick()




