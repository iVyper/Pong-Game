"""
Main Module for Pong Game

Sets up the game screen, paddles, ball, and scoreboard. Runs the main game loop,
handling movement, collision detection, scoring, and screen updates.
"""

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create and configure the game window
screen = Screen()
screen.title("Pong Game")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)  # Turn off automatic screen updates

# Instantiate paddles for player 1 (left) and player 2 (right)
player1_paddle = Paddle()
player2_paddle = Paddle()

# Set up keyboard controls for both paddles
screen.listen()
screen.onkey(player1_paddle.up, "w")
screen.onkey(player1_paddle.down, "s")
screen.onkey(player2_paddle.up, "Up")
screen.onkey(player2_paddle.down, "Down")

# Create the ball and scoreboard
ball = Ball()
scoreboard = Scoreboard()

# Main game loop flag
game = True
while game:
    time.sleep(ball.ball_speed)  # Control the game's speed
    screen.update()              # Manually refresh the screen
    ball.move()                  # Advance the ball

    # Bounce off top and bottom walls
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # Bounce off paddles
    hit_left_paddle = (ball.distance(player1_paddle) < 50 and ball.xcor() < -320)
    hit_right_paddle = (ball.distance(player2_paddle) < 50 and ball.xcor() > 320)
    if hit_left_paddle or hit_right_paddle:
        ball.bounce_x()

    # Check for left wall exit (player 2 scores)
    if ball.xcor() < -380:
        scoreboard.player2_scored()
        ball.reset_pos()

    # Check for right wall exit (player 1 scores)
    if ball.xcor() > 380:
        scoreboard.player1_scored()
        ball.reset_pos()

# Keep the window open until clicked
screen.exitonclick()
