from turtle import Turtle, Screen
import random

def start_race():
    screen.clear()
    screen.bgcolor("black")
    colors = ["red", "blue", "green", "yellow", "cyan", "purple"]
    y_positions = [-70, -40, -10, 20, 50, 80]
    all_turtles = []

    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-380, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)

    user_bet = screen.textinput(title="Make your bet", prompt=f"Choose a color: {', '.join(colors)} ")
    is_race_on = bool(user_bet)

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 380:
                is_race_on = False
                winning_turtle = turtle.pencolor()
                if winning_turtle == user_bet:
                    screen.textinput("🏁 Result", f"🏆You've won! The winning turtle is {winning_turtle}.")
                else:
                    screen.textinput("🏁 Result", f"😕You've lost! The winning turtle is {winning_turtle}.")
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

screen = Screen()
screen.setup(width=800, height=500)

while True:
    start_race()
    restart_race = screen.textinput(title="🏁", prompt="If you wanna try again type 'y', else type 'n':")
    if not restart_race or restart_race.lower() != 'y':
        screen.bye()
        break