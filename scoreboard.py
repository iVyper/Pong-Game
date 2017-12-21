"""
Scoreboard Module

Defines the Scoreboard class that displays and updates player scores
on the game screen.
"""

from turtle import Turtle


class Scoreboard(Turtle):
    """
    Manages and displays the scores for both players.

    Attributes:
        player1_score (int): Score for left paddle.
        player2_score (int): Score for right paddle.
    """

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()  # We only write text, no visible turtle
        self.player1_score = 0
        self.player2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Clears the old scores and writes the updated scores at the top of the screen.
        """
        self.clear()
        # Left player score
        self.goto(-100, 200)
        self.write(self.player1_score, align="center", font=("Arial", 24, "bold"))
        # Right player score
        self.goto(100, 200)
        self.write(self.player2_score, align="center", font=("Arial", 24, "bold"))

    def player1_scored(self):
        """
        Increment player 1's score and refresh the display.
        """
        self.player1_score += 1
        self.update_scoreboard()

    def player2_scored(self):
        """
        Increment player 2's score and refresh the display.
        """
        self.player2_score += 1
        self.update_scoreboard()
