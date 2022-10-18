import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
# Creating variables and the Game stuffs
game_on = True
ekran = Screen()
ekran.title("PONG")
ekran.screensize(canvwidth=800, canvheight=600)
ekran.bgcolor("black")
ekran.tracer(0)
paddle1 = Paddle()
paddle2 = Paddle()
gameBall = Ball()
skorbord=Scoreboard()
# Creating over

# Listening to keys
ekran.listen()
ekran.onkeypress(paddle1.moveup, "Up")
ekran.onkeypress(paddle1.movedown, "Down")
ekran.onkeypress(paddle2.moveup, "w")
ekran.onkeypress(paddle2.movedown, "s")

# Listening over
# Game Starts
while game_on:
    time.sleep(0.028)
    ekran.update()
    gameBall.move()
    if gameBall.ycor() > 375 or gameBall.ycor() < -375:
        gameBall.collision_with_wall()
    if gameBall.distance(paddle1) < 50 and gameBall.xcor() > 340:
        gameBall.collision_with_paddle()
    elif gameBall.distance(paddle2) < 50 and gameBall.xcor() < -340:
        gameBall.collision_with_paddle()
    if gameBall.xcor()>450:
        gameBall.reset_ball()
        skorbord.left_paddle_scores()
    elif gameBall.xcor()<-450:
        gameBall.reset_ball()
        skorbord.right_paddle_scores()
ekran.exitonclick()
# Game over
