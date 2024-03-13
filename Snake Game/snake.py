from turtle import Turtle

class Snake:

    def __init__(self) -> object:
        self.segments = []
        self.start_positions = [(0, 0), (-20, 0), (-40, 0)]

    def create(self):
        for position in self.start_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def extend(self):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(self.segments[-1].position())
        self.segments.append(new_seg)

    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
