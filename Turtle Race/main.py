from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=800, height=400)
finish_line = Turtle()
finish_line.shape("square")
finish_line.color("red")
finish_line.shapesize(stretch_wid=15, stretch_len=0.1)
finish_line.penup()
finish_line.goto(350, 20)
finish_line.write("  FINISH")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose a color: \n "
                                                          "red/orange/yellow/green/blue/purple/pink/brown")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"]
y_position = [-70, -40, -10, 20, 50, 80, 110, 140]
all_turtles = []

for turtle_index in range(0, 8):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-300, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 270:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                turtle.write("    Congratulation you\nare the WINNER")
            else:
                turtle.write(f" You have lost!\n{winning_color} is the WINNER")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
