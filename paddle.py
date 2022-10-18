from turtle import Turtle


positions = [(400, 0), (-400, 0)]


class Paddle(Turtle):

    def __init__(self):

        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(positions[0])
        self.showturtle()
        self.setheading(90)
        self.turtlesize(stretch_wid=1, stretch_len=7.5)
        positions.pop(0)

    def moveup(self):
        if self.ycor()<325:
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)

    def movedown(self):
        if self.ycor()>-325:
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)
