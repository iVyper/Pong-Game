"""
Paddle Module

Defines the Paddle class used by both players. Handles paddle creation,
positioning, and vertical movement.
"""

from turtle import Turtle

PADDLE_HEIGHT = 100  # Paddle height in pixels
PADDLE_WIDTH = 20  # Paddle width in pixels

# Global list to track created paddles for positioning logic
paddles = []


class Paddle(Turtle):
    """
    Represents a player paddle in Pong. Inherits from Turtle.

    Methods:
        up(): Move the paddle up.
        down(): Move the paddle down.
    """

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        # Scale to the desired paddle dimensions
        self.shapesize(stretch_wid=PADDLE_WIDTH / 20, stretch_len=PADDLE_HEIGHT / 20)
        paddles.append(self)  # Keep track of this paddle
        self.set_paddle_position()  # Place on left or right edge
        self.setheading(90)  # Face the paddle "up" by default

    def up(self):
        """Move the paddle up by 20 pixels."""
        self.forward(20)

    def down(self):
        """Move the paddle down by 20 pixels."""
        self.backward(20)

    def set_paddle_position(self):
        """
        Positions this paddle on the left or right side of the screen
        based on whether it's the first or second paddle created.
        """
        if self == paddles[0]:
            self.goto(-350, 0)  # Left side
        elif self == paddles[1]:
            self.goto(350, 0)  # Right side
