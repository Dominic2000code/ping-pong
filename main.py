from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)

paddle_r = Paddle((-350, 0))
paddle_l = Paddle((350, 0))

screen.listen()
screen.onkey(paddle_l.up, "Up")
screen.onkey(paddle_l.down, "Down")
screen.onkey(paddle_r.up, "w")
screen.onkey(paddle_r.down, "s")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()
