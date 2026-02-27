from __future__ import annotations
import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self, screen_width: int, screen_height: int, cell_size: int = 20):
        super().__init__()

        # save settings
        self.cell_size = cell_size

        # appearance
        self.shape("circle")
        self.penup()
        self.speed("fastest")

        # size smaller than snake
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

        # keep inside screen bounds
        self._half_w = (screen_width // 2) - cell_size
        self._half_h = (screen_height // 2) - cell_size

        # initial spawn
        self.refresh(set())

    # spawn new food, avoiding snake body
    def refresh(self, occupied_positions: set[tuple[int, int]]):
        fruit_type = random.choice(["orange", "plum", "strawberry", "sparkly"])

        if fruit_type == "orange":
            self.color("orange")
            self.points = 2
            self.shapesize(0.5, 0.5)

        elif fruit_type == "plum":
            self.color("purple")
            self.points = 2
            self.shapesize(0.5, 0.5)

        elif fruit_type == "strawberry":
            self.color("red")
            self.points = 3
            self.shapesize(0.5, 0.5)

        elif fruit_type == "sparkly":
            self.color("gold")
            self.points = 5
            self.shapesize(0.7, 0.7)

        # snap to grid & avoid snake
        while True:
            x = random.randrange(-self._half_w, self._half_w, self.cell_size)
            y = random.randrange(-self._half_h, self._half_h, self.cell_size)

            if (x, y) not in occupied_positions:
                self.goto(x, y)
                break
            