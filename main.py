from time import time

# Screen constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20


class Game:
    def __init__(self):
        # Initialize game with screen, snake, food, and scoreboard
        pass

    # main game loop
    # keeps updating the screen and checking collisions
    def run(self) -> None:
        while self.game_is_on:
            self.screen.update()
            time.sleep(self.game_speed)
            self.snake.move()

            self._check_collisions()

        self.screen.mainloop()

# checks all types of collisions
def _check_collisions(self) -> None:
    self._check_food_collision()
    self._check_wall_collision()
    self._check_self_collision()

# checks if snake eats the food
def _check_food_collision(self) -> None:
    if self.snake.head.distance(self.food) < 15:
        self.snake.extend()

        # add points based on the food type
        self.scoreboard.increase_score(self.food.points)

        # collect all snake positions so no free food spawns on it
        occupied = {(int(seg.xcor()), int(seg.ycor())) for seg in self.snake.segments}

    self.food.refresh(occupied)

# checks if snake hits the wall
def _check_wall_collision(self) -> None:
    half_w = SCREEN_WIDTH / 2
    half_h = SCREEN_HEIGHT / 2

    x = self.snake.head.xcor()
    y = self.snake.head.ycor()

    if (x > half_w - CELL_SIZE or x < -half_w + CELL_SIZE or y > half_h - CELL_SIZE 
        or y < -half_h + CELL_SIZE):
        self._restart()

# checks if snake hits its own body
def _check_self_collision(self) -> None:
    for segment in self.snake.segments[1:]:
        if self.snake.head.distance(segment) < 10:
            self._restart()
        break

# resets the game after collision
def _restart(self) -> None:
    self.snake.reset()
    self.scoreboard.reset()

    occupied = {(int(seg.xcor()), int(seg.ycor())) for seg in self.snake.segments}

    self.food.refresh(occupied)


# start the super cool game
if __name__ == "__main__":
    game = Game()
    game.run()