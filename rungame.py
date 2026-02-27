from __future__ import annotations
import time
import matplotlib.pyplot as plt
from turtle import Screen
from snake import Snake
from food import Food
from screen import Scoreboard  


# Game constants

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20
MOVE_DISTANCE = CELL_SIZE


# Game class (runner)

class Game:
    def __init__(self):
        # Screen setup
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Advanced Snake Game")
        self.screen.tracer(0)

        # Create objects from old files
        self.snake = Snake()
        self.food = Food(SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE)
        self.scoreboard = Scoreboard()

        # Controls
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")

        # Game state
        self.game_speed = 0.1
        self.game_is_on = True

        # Stats
        self.food_eaten = 0
        self.total_movement = 0
        self.start_time = time.time()

    #main game loop
    def run(self) -> None:
        while self.game_is_on:
            self.screen.update()
            time.sleep(self.game_speed)

            # move snake and track movement
            self.snake.move()
            self.total_movement += MOVE_DISTANCE

            # check all collisions
            self._check_collisions()

        # End game summary
        self._end_summary()
        self.screen.bye()

    # check collisions
    def _check_collisions(self) -> None:
        self._check_food_collision()
        self._check_wall_collision()
        self._check_self_collision()

    # snake eats food
    def _check_food_collision(self) -> None:
        if self.snake.head.distance(self.food) < 15:
            self.snake.extend()
            self.scoreboard.increase_score(self.food.points)
            self.food_eaten += 1

            # avoid spawning food inside snake
            occupied = {(int(seg.xcor()), int(seg.ycor())) for seg in self.snake.segments}
            self.food.refresh(occupied)

    # wall collision
    def _check_wall_collision(self) -> None:
        half_w = SCREEN_WIDTH / 2
        half_h = SCREEN_HEIGHT / 2
        x, y = self.snake.head.xcor(), self.snake.head.ycor()

        if x > half_w - CELL_SIZE or x < -half_w + CELL_SIZE or y > half_h - CELL_SIZE or y < -half_h + CELL_SIZE:
            self._restart()

    # self collision
    def _check_self_collision(self) -> None:
        for segment in self.snake.segments[1:]:
            if self.snake.head.distance(segment) < 10:
                self._restart()
                break

    # restart game
    def _restart(self) -> None:
        self.snake.reset()
        self.scoreboard.reset()
        occupied = {(int(seg.xcor()), int(seg.ycor())) for seg in self.snake.segments}
        self.food.refresh(occupied)

    # show matplotlib summary
    def _end_summary(self) -> None:
        duration = time.time() - self.start_time
        labels = ["Food Eaten", "Duration (seconds)", "Total Movement"]
        values = [self.food_eaten, round(duration, 2), self.total_movement]

        plt.figure()
        plt.bar(labels, values)
        plt.title("Snake Game Summary")
        plt.ylabel("Value")
        for i in range(len(values)):
            plt.text(i, values[i], str(values[i]), ha="center", va="bottom")
        plt.show()



# Run the beautiful game

if __name__ == "__main__":
    game = Game()
    game.run()