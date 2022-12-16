from turtle import Turtle

INI_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in INI_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        seg = Turtle(shape="square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.segments.append(seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_n in range(len(self.segments) - 1, 0, -1):
            nx = self.segments[seg_n - 1].xcor()
            ny = self.segments[seg_n - 1].ycor()
            self.segments[seg_n].goto(nx, ny)
        self.segments[0].forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
