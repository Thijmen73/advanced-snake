
#what is this code resposible for?
#Where food appears
#Making sure it doesn’t spawn inside the snake
#Handling its own color
#Snapping to the grid



from __future__ import annotations

import random
import tkinter 
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

  # keep food inside the screen bounds (in turtle coordinates)
  # example: for 600x600 screen, x/y normally go from about -300 to +300
  # subtract cell_size so food never appears cut off at the edges 
self._half_w = (screen_width // 2) - cell_size
self._half_h = (screen_height // 2) - cell_size

   # place the first food somewhere random
self.refresh(set())


# 

# making sure the food does not spawn on the snake 
    def refresh(self, occupied_positions):
    
    # the different food types, and the points they give, including the sparkly strawberry which gives 5 points instead of 3 
 
 #pick a food type
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

#SPARKLY STRAWBERRY, YESSSS
    elif fruit_type == "sparkly":
        self.color("gold")
        self.points = 5
        self.shapesize(0.7, 0.7)
    

    #snap to the grid, and make sure its avoids the snake body
    while True:
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)

        if (x, y) not in occupied_positions:
            self.goto(x, y)
            break