from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        nx = self.xcor() + self.x_move
        ny = self.ycor() + self.y_move
        self.goto(nx, ny)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
