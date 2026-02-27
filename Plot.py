import turtle
import time
import random
import matplotlib.pyplot as plt
from snake import Snake

# creating the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game With Summary")
screen.tracer(0)

# tracking game statistics
food_eaten = 0
total_movement = 0
game_start_time = time.time()

# create snake
jerry = Snake()

# create food
food = turtle.Turtle("circle")
food.color("red")
food.penup()
food.shapesize(0.5, 0.5)
food.speed("fastest")
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# connect keyboard to snake movement
screen.listen()
screen.onkey(jerry.up, "Up")
screen.onkey(jerry.down, "Down")
screen.onkey(jerry.left, "Left")
screen.onkey(jerry.right, "Right")


# shows matplotlib summary after game ends
def show_summary(food_eaten, duration, total_movement):
    labels = ["Food Eaten", "Duration (seconds)", "Total Movement"]
    values = [food_eaten, round(duration, 2), total_movement]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Snake Game Summary")
    plt.ylabel("Value")

    # show numbers above bars
    for i in range(len(values)):
        plt.text(i, values[i], str(values[i]), ha="center", va="bottom")

    plt.show()


# main game loop
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    jerry.move()
    total_movement += 20

    # border collision
    if abs(jerry.head.xcor()) > 290 or abs(jerry.head.ycor()) > 290:
        game_on = False

    # food collision
    if jerry.head.distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        jerry.extend()
        food_eaten += 1

    # self collision
    for segment in jerry.segments[1:]:
        if jerry.head.distance(segment) < 10:
            game_on = False


# game ended
game_end_time = time.time()
duration = game_end_time - game_start_time

screen.bye()  # close turtle window

# show matplotlib summary
show_summary(food_eaten, duration, total_movement)