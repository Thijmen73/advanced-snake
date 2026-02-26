from __future__ import annotations

import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self, screen_width: int, screen_height: int, cell_size: int = 20):
        super().__init__()
 # save settings so we can reuse them later, if needed 
      self.cell_size = cell_size
    
# how the turtle food will look like 
   self.shape("circle")
   self.penup()
   self.speed("fastest")
   self.color("red")


 # The default turtle size is ~20x20, which is bigger, so to make the food smaller, 0.5 makes it ~10x10
    self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    