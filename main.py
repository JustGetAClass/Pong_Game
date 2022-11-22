from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.r_move()

    # Detect collision with floor and ceiling
    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce the ball
        ball.bounce_y()

    # Detect collision with r_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        # bounce from paddle
        ball.bounce_x()

    # r_paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()
        score.add_score2()
    # r_paddle misses
    elif ball.xcor() < -380:
        ball.reset_pos()
        score.add_score1()

screen.exitonclick()
