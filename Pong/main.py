from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Track keys being held down for smooth movement
keys_pressed = {"Up": False, "Down": False, "w": False, "s": False}

def key_press(key):
    if key in keys_pressed:
        keys_pressed[key] = True

def key_release(key):
    if key in keys_pressed:
        keys_pressed[key] = False

screen.listen()
screen.onkeypress(lambda: key_press("Up"), "Up")
screen.onkeyrelease(lambda: key_release("Up"), "Up")
screen.onkeypress(lambda: key_press("Down"), "Down")
screen.onkeyrelease(lambda: key_release("Down"), "Down")
screen.onkeypress(lambda: key_press("w"), "w")
screen.onkeyrelease(lambda: key_release("w"), "w")
screen.onkeypress(lambda: key_press("s"), "s")
screen.onkeyrelease(lambda: key_release("s"), "s")

def quit_game():
    global game_is_on
    game_is_on = False
    screen.bye()

screen.onkey(quit_game, "q")

game_is_on = True
frame_count = 0
while game_is_on:
    frame_count += 1
    time.sleep(0.03)
    screen.update()
    ball.move()
    # AI only moves every other frame to make it weaker
    if frame_count % 2 == 0:
        r_paddle.ai_move(ball.ycor())
    
    #check if keys are held down
    if keys_pressed["Up"]:
        l_paddle.go_up()
    if keys_pressed["Down"]:
        l_paddle.go_down()
    if keys_pressed["w"]:
        l_paddle.go_up()
    if keys_pressed["s"]:
        l_paddle.go_down()

    # Collision with top and bottom walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    # Collision with paddles
    """Right Paddle"""
    if (ball.xcor() > 320 and ball.xcor() < 340) and (ball.ycor() < r_paddle.ycor() + 50 and ball.ycor() > r_paddle.ycor() - 50):
        ball.paddle_hit()
    """Left Paddle"""
    if (ball.xcor() < -320 and ball.xcor() > -340) and (ball.ycor() < l_paddle.ycor() + 50 and ball.ycor() > l_paddle.ycor() - 50):
        ball.paddle_hit()

    # Detect when right paddle missed (AI loses)
    if ball.xcor() > 380:
        scoreboard.increase_player_score()
        ball.reset_position()

    # Detect when left paddle missed (Player loses)
    if ball.xcor() < -380:
        scoreboard.increase_ai_score()
        ball.reset_position()
    

screen.exitonclick()



