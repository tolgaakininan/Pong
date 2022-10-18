from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.leftScore = 0
        self.rightScore = 0
        self.write_scoreboard()

    def write_scoreboard(self):
        self.clear()
        self.goto(-100, 300)
        self.write(self.leftScore, align="Center", font=("Courier", 80, "normal"))
        self.goto(100, 300)
        self.write(self.rightScore, align="Center", font=("Courier", 80, "normal"))

    def left_paddle_scores(self):
        self.leftScore += 1
        self.write_scoreboard()

    def right_paddle_scores(self):
        self.rightScore += 1
        self.write_scoreboard()
