from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")

        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def collision_with_wall(self):
        self.y_move *= -1
        self.move()
    def collision_with_paddle(self):
        self.x_move *= -1
        self.move()
    def reset_ball(self):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        self.collision_with_paddle()
