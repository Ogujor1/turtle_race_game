# Import the necessary Class for Building the Game

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=550, height=550)

is_race_on = False

# Creating the turtles with different colours

colour = ['red', 'blue', 'green', 'purple', 'black']
y_position = [-100, -30, 40, 110, 170]

user_bet = screen.textinput(title='Turtle Race Game', prompt='Pick a Turtle Color\n"Red, Green, Black, Purple, Blue" ').lower()


all_turtle = []
for turtle_position in range(5):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colour[turtle_position])
    new_turtle.goto(x=-260, y=y_position[turtle_position])
    all_turtle.append(new_turtle)

# Starting the race and moving the turtles

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        move_turtle = random.randint(0, 10)
        turtle.forward(move_turtle)

# Declaring the endpoint for the turtles and winner of the race

        if turtle.xcor() > 248:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f" You won!!, {winner.title()}!, won the race")
            else:
                print(f"You lose!!, {winner.title()}!, won the race")


screen.exitonclick()
