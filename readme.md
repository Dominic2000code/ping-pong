
---

# Ping-Pong Game with Python and Turtle - 100 days of python

This is a classic Ping-Pong game implemented using Python and Turtle graphics.

## Overview

The Ping-Pong game consists of the following files:

- `main.py`: Main script to run the game.
- `paddle.py`: Defines the Paddle class and its functionalities.
- `ball.py`: Defines the Ball class and its functionalities.
- `scoreboard.py`: Defines the Scoreboard class to keep track of the players' scores.

## Running the Game

To play the game, run the `main.py` script. You can control the left paddle using the "W" and "S" keys, and control the right paddle using the Up and Down arrow keys. The objective is to bounce the ball with the paddles and avoid missing it.

## Files Description

### `main.py`

- Initializes the game screen.
- Creates instances of the Paddle, Ball, and Scoreboard classes.
- Listens for keyboard input to control the paddles' movement.
- Checks for collisions and updates the game state accordingly.

### `paddle.py`

- Defines the Paddle class.
- Initializes the paddle's attributes such as shape, color, and position.
- Contains methods to move the paddle up and down based on keyboard input.

### `ball.py`

- Defines the Ball class.
- Initializes the ball's attributes such as shape, color, and movement speed.
- Contains methods to move the ball, bounce off walls, and bounce off paddles.

### `scoreboard.py`

- Defines the Scoreboard class.
- Initializes the scores for the left and right players.
- Contains methods to increment the scores and update the scoreboard display.

## Dependencies

The game requires the Turtle module, which is included in the Python Standard Library.

## Gameplay

- Use the "W" and "S" keys to control the left paddle.
- Use the Up and Down arrow keys to control the right paddle.
- Bounce the ball with the paddles to prevent it from passing.
- Score points when the opposing player misses the ball.
- The game ends when one player reaches the maximum score.

---
