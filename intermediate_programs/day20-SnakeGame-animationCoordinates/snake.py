# Set as Constant
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []      # attribute, use self when working with a class
        self.create_snake()
        self.head = self.segments[0]    # head of snake is first segment

    def create_snake(self):
        # create a segment of the snake recursively
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # ----- DAY 24 -----
    # redo the initialization
    def reset(self):
        for seg in self.segments:
            # move old segments off the screen
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # add a new segment to the snake, adding to the last segment [1,2,3] -> add after 3
        self.add_segment(self.segments[-1].position())

    def move(self):
        # segment3 -> position of segment2
        # segment2 -> position of segment1
        # segment1 -> go forward 20 paces

        # if we want range of 123 then start=1, stop=3, step=1
        # (0, 0) -> 0, (-20, 0) -> 1, (-40, 0) -> 2      ***note list starts at 0 so this is [0,1,2]
        # start=2, stop=0, step=-1
        # for loop only deals with segment 3 and segment 2, segment 1 will then move forward
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # segment at [1] get x coordinate
            new_y = self.segments[seg_num - 1].ycor()  # segment at [1] get y coordinate
            self.segments[seg_num].goto(new_x, new_y)  # get last segment and get it to position of 2nd to last segment
        self.segments[0].forward(MOVE_DISTANCE)
        # segments[0].left(90)

    def up(self):
        # if pointing down it can move up, if it's set to down it can't move up
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

# ----- EXTRA NOTES -----
# # initialize the snake
# segment_1 = Turtle(shape="square")
# segment_1.color("white")
#
# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(-20, 0)
#
# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.goto(-40, 0)