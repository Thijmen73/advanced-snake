from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self._colors = ("darkblue", "gray")

        self.create_snake()
        self.head = self.segments[0]
        self.head.setheading(RIGHT)

        self._alternate_colors()

    # creates the initial snake body
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # adds a new turtle segment
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # extends snake when eating food
    def extend(self):
        self.add_segment(self.segments[-1].position())
        self._alternate_colors()

    # handles movement
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    # direction controls
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # alternates segment colors
    def _alternate_colors(self):
        for index, segment in enumerate(self.segments):
            color_index = index % len(self._colors)
            segment.color(self._colors[color_index])