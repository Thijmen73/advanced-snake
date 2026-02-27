import turtle
import time
import random
import matplotlib.pyplot as plt

# Game setup

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

food_eaten = 0
total_movement = 0
game_start_time = time.time()

# snake
segments = []

def create_segment(position):
    segment = turtle.Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for pos in starting_positions:
    create_segment(pos)

head = segments[0]
head.direction = "stop"

# food summary

food = turtle.Turtle("circle")
food.color("red")
food.penup()
food.shapesize(0.5, 0.5)
food.speed("fastest")
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# summary movement

def move():
    global total_movement
    
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if head.direction == "up":
        head.sety(head.ycor() + 20)
        total_movement += 20
    if head.direction == "down":
        head.sety(head.ycor() - 20)
        total_movement += 20
    if head.direction == "left":
        head.setx(head.xcor() - 20)
        total_movement += 20
    if head.direction == "right":
        head.setx(head.xcor() + 20)
        total_movement += 20

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

def show_summary(food_eaten, duration, total_movement):
    labels = ['Food Eaten', 'Duration (seconds)', 'Total Movement']
    values = [food_eaten, round(duration, 2), total_movement]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Snake Game Summary")
    plt.ylabel("Value")

    # Show numbers on bars
    for i in range(len(values)):
        plt.text(i, values[i], str(values[i]), ha='center', va='bottom')

    plt.show()

# -------------------- GAME LOOP --------------------

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    move()

    # Border collision
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        game_on = False

    # Food collision
    if head.distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        create_segment(segments[-1].position())
        food_eaten += 1

    # Self collision
    for segment in segments[1:]:
        if head.distance(segment) < 10:
            game_on = False


game_end_time = time.time()
duration = game_end_time - game_start_time

screen.bye()  # Close turtle window
show_summary(food_eaten, duration, total_movement)