from turtle import Turtle
#defining numbers in terms easy to understand.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self._colors=["darkblue","gray"]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            self.head.setheading(RIGHT)
    @property
    def _colors(self):
        return self.__colors
    @_colors.setter
    def _colors(self, color_tuple):
        self.__colors = color_tuple
        if isinstance(color_tuple, tuple):
            for index, segment in enumerate(self.segments) and len(color_tuple)==2:
                self.__colors=color_tuple
                self._alternate_colors()
            else:
                raise ValueError("colors must be provided in a pair of color strings")
    def _alternate_colors(self):
        for index, segment in enumerate(self.segments):
            color_index = index % len(self.__colors)
            segment.color(self.__colors[color_index])
    # defines how a new segment is added to the snake and describes it
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    #defines how the new segment is added to the front of the snake.
    def extend(self):
        self.add_segment(self.segments[-1].position()) 
    #defines how the snake moves forward by moving each segment to the position of the previous one.
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    #defines changes in direction while preventing backtracking and selfdestruction.
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
    
