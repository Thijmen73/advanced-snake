import turtle
import time
import matplotlib.pyplot as plt
from snake import Snake
from food import Food

# screen setup
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 20

screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Advanced Snake With Summary")
screen.tracer(0)

# stats tracking
food_eaten = 0
total_movement = 0
game_start_time = time.time()

# create snake
jerry = Snake()

# create food using your Food class
food = Food(SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE)

# controls
screen.listen()
screen.onkey(jerry.up, "Up")
screen.onkey(jerry.down, "Down")
screen.onkey(jerry.left, "Left")
screen.onkey(jerry.right, "Right")


def show_summary(food_eaten, duration, total_movement):
    labels = ["Food Eaten", "Duration (seconds)", "Total Movement"]
    values = [food_eaten, round(duration, 2), total_movement]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Snake Game Summary")
    plt.ylabel("Value")

    for i in range(len(values)):
        plt.text(i, values[i], str(values[i]), ha="center", va="bottom")

    plt.show()


# game loop
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
        food_eaten += 1
        jerry.extend()

        # pass snake positions so food avoids spawning on snake
        snake_positions = {
            (segment.xcor(), segment.ycor())
            for segment in jerry.segments
        }

        food.refresh(snake_positions)

    # self collision
    for segment in jerry.segments[1:]:
        if jerry.head.distance(segment) < 10:
            game_on = False


# end game
game_end_time = time.time()
duration = game_end_time - game_start_time

screen.bye()
show_summary(food_eaten, duration, total_movement)