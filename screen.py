from __future__ import annotations


# :creating the screen, connecting snake, food and scoreboard together, handling collisions
# restarting the game, running the main game loop

import time
from turtle import Screen, Turtle

from snake import Snake
from food import Food


# game grid settings
# the snake moves in steps of 20, so everything is based on this grid
GRID_WIDTH = 30
GRID_HEIGHT = 30
CELL_SIZE = 20

SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE


# scoreboard class
# keeps track of your current score and of the high score
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.score_history={0:0}
        self.round_number=0

        self.hideturtle()
        self.penup()
        self.color("white")

        # position the score at the top of the screen
        self.goto(0, SCREEN_HEIGHT / 2 - 40)
        self._draw()

    #draws or updates the score text
    def _draw(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center"
                   , font=("Arial", 16, "normal"))

    # increase score when food is eaten
    def increase_score(self, points: int):
        self.score += points

        # update high score if needed
        if self.score > self.high_score:
            self.high_score = self.score

        self._draw()

    # reset score when the snake crashes and dies
    def reset(self):
        self.score_history.append({"round": self.round_number, "score": self.score})
        self.round_number += 1
        self.score = 0
        self._draw()


# main game controller
# to connect everything together
class Game:
    def __init__(self):
        self.screen = Screen()
        self._setup_screen()

        # create game objects
        self.snake = Snake()
        self.food = Food(SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE)
        self.scoreboard = Scoreboard()

        self._setup_controls()

        # controls how fast the snake moves
        self.game_speed = 0.1
        self.game_is_on = True

    # sets up the screen appearance
    def _setup_screen(self) -> None:
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Advanced Snake Game")
        self.screen.tracer(0)

    # connects arrow keys to snake movement
    def _setup_controls(self) -> None:
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")
