from turtle import Screen, Turtle
from paddlegame import PaddleGame
from ballgame import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)


def wall(p, c):
    p.shape("square")
    p.color(c)
    p.pencolor('black')
    p.shapesize(stretch_wid=2, stretch_len=4)


red_wall = []
for _ in range(0, 10):
    red_wall.append(Turtle())

x = -380
for p in red_wall:
    x += 70
    wall(p, "red")
    p.goto(x, 250)


orange_wall = []
for _ in range(0, 10):
    orange_wall.append(Turtle())

x = -380
for p in orange_wall:
    x += 70
    wall(p, "orange")
    p.goto(x, 210)

yellow_wall = []
for _ in range(0, 10):
    yellow_wall.append(Turtle())

x = -380
for p in yellow_wall:
    x += 70
    wall(p, "yellow")
    p.goto(x, 170)

green_wall = []
for _ in range(0, 10):
    green_wall.append(Turtle())

x = -380
for p in green_wall:
    x += 70
    wall(p, "green")
    p.goto(x, 130)

blue_wall = []
for _ in range(0, 10):
    blue_wall.append(Turtle())

x = -380
for p in blue_wall:
    x += 70
    wall(p, "blue")
    p.goto(x, 90)


def contact_wall(l, y):
    for p in l:
        if ball.distance(p) < 50 and ball.ycor() > y:
            ball.bounce_y()
            p.color('black')
            l.remove(p)


paddle = PaddleGame()
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280:
        ball.bounce_y()
    elif ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.distance(paddle) < 50 and ball.ycor() > -280:
        ball.bounce_y()

    contact_wall(blue_wall, 70)
    contact_wall(green_wall, 110)
    contact_wall(yellow_wall, 150)
    contact_wall(orange_wall, 190)
    contact_wall(red_wall, 230)

    if ball.ycor() < -300:
        scoreboard.lose()
        game_is_on = False
    elif len(blue_wall) == 0 and len(green_wall) == 0 and len(yellow_wall) == 0 and len(orange_wall) == 0 and len(red_wall) == 0:
        scoreboard.win()
        game_is_on = False


screen.exitonclick()
