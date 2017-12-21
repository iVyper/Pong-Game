"""
Ball Module

Defines the Ball class that handles movement, collisions, and reset behavior
for the Pong ball in the game.
"""

from turtle import Turtle
from paddle import PADDLE_HEIGHT, PADDLE_WIDTH

BALL_SIZE = 20  # Diameter of the ball in pixels


class Ball(Turtle):
    """
    Represents the Pong ball. Inherits from Turtle to leverage built‑in drawing
    and coordinate functionality.

    Attributes:
        x_move (int): Horizontal movement step.
        y_move (int): Vertical movement step.
        ball_speed (float): Delay between moves (lower is faster).
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        # Scale the circle to the desired ball size
        self.shapesize(stretch_wid=BALL_SIZE / 20, stretch_len=BALL_SIZE / 20)
        self.penup()
        # Initial movement deltas
        self.x_move = 10
        self.y_move = 10
        # Initial speed (seconds between screen updates)
        self.ball_speed = 0.1

    def move(self):
        """
        Moves the ball by its current x_move and y_move values.
        Called on each frame to update position.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Reverses the vertical direction of the ball.
        Called when the ball hits the top or bottom wall.
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Reverses the horizontal direction of the ball and speeds it up slightly.
        Called when the ball collides with a paddle.
        """
        self.x_move *= -1
        self.ball_speed *= 0.9  # Increase game difficulty over time

    def reset_pos(self):
        """
        Resets the ball to the center and reverses the horizontal direction.
        Also restores the initial ball speed.
        Called when a point is scored.
        """
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
