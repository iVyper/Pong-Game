
# Pong Game
Pong Game is a classic two-player arcade game recreated using Python’s turtle graphics library. Two paddles are controlled via keyboard inputs on either side of the screen, and a ball bounces back and forth, speeding up each time it hits a paddle. Players score points when their opponent misses the ball. The first to an arbitrary score (or just play indefinitely) tests reflexes and timing in this faithful digital rendition.

## Features
- **Two-Player Controls:**
   - **Left Paddle:** ‘W’ to move up, ‘S’ to move down
   - **Right Paddle:** Up‑Arrow to move up, Down‑Arrow to move down
- **Realistic Ball Physics:**
   - Bounces off top and bottom walls
   - Reverses direction and slightly increases speed each time it hits a paddle
- **Scoring System:**
   - Points awarded when the ball passes beyond the opponent’s paddle
   - Live scoreboard displayed at the top of the window
- **Reset on Score:**
   - Ball resets to center after each score, maintaining momentum and pace
- **Clean Visuals:**
   - Black background with white paddles, ball, and scoreboard for high contrast


## Installation

### Prerequisites

- **Python 3.x:** Ensure that Python 3 is installed on your system. You can download it from [Python's offical website](python.org).

- **Turtle Module:** Included in the Python standard library

- **Time Module:** Part of Python’s standard library (used for pacing the game loop)
### How to Run

1. **Download the Code:** Clone the repository or make sure you have the following files in a single directory:
- `main.py`

- `ball.py`

- `paddle.py`

- `scoreboard.py`

2. **Open Terminal/Command Prompt:** Navigate to the directory containing the file.

3. **Run the program:** Execute the following command:

    ```bash
    python3 main.py
    ```

4. **Play:**
   - Use `W`/`S` keys to move the left paddle up/down.

   - Use Up/Down arrow keys to move the right paddle.

   - Watch the ball bounce and score points when it passes a paddle.

   - The scoreboard at the top updates in real time.

5. **Exit:**
Click the game window or close the terminal once you’re done.


## Demo
![Pong Game Demo](screenshots/demo.gif)

## License

This project is open-source and available under the [MIT License](https://choosealicense.com/licenses/mit/).


## Authors

- Ivis Perdomo [@ivyper](https://www.github.com/ivyper)

