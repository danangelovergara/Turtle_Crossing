# Pong Game

A classic Pong game built with Python's Turtle graphics library. Play against an AI opponent and try to score points!

## Requirements

- Python 3.x
- turtle (built-in with Python)

## Installation

1. Make sure you have Python 3 installed
2. No additional packages needed - the game uses only built-in libraries
3. run main.py

## How to Play

### Controls
- **Up Arrow** or **W** - Move paddle up
- **Down Arrow** or **S** - Move paddle down
- **Q** - Quit the game

### Game Rules
- Use your paddle (left side) to hit the ball back to the AI
- The AI controls the right paddle
- Score a point when the opponent misses
- The ball gets faster with each paddle hit
- First to reach the most points wins!

## Customization

You can modify the game difficulty and behavior by editing `main.py`:

### Screen Size
In `main.py`, line 11-12:
```python
screen.setup(width=800, height=600)  # Change width and height here
```

### Ball Speed (Initial Velocity)
In `ball.py`, lines 12-13:
```python
self.x_move = 10    # Change horizontal speed (increase = faster)
self.y_move = 10    # Change vertical speed (increase = faster)
```

### Ball Acceleration on Paddle Hit
In `ball.py`, in the `paddle_hit()` method:
```python
self.x_move *= 1.1  # Change 1.1 to increase/decrease acceleration (1.05 = slower, 1.2 = faster)
```

### AI Difficulty
In `paddle.py`, in the `ai_move()` method:
```python
if self.ycor() < ball_y - 70:  # Decrease 70 to make AI better, increase to make weaker
    self.go_up()
elif self.ycor() > ball_y + 70:  # Same here
    self.go_down()
```

In `main.py`, in line 54
```python
    if frame_count % 2 == 0:
        r_paddle.ai_move(ball.ycor()) #changes how much ai moves, 1 would make it the hardest going up would make it weaker
```

### Paddle Movement Speed
In `paddle.py`, in the `go_up()` and `go_down()` methods:
```python
new_y = self.ycor() + 20  # Change 20 to increase/decrease paddle speed
```

## Game Files

- `main.py` - Main game loop and collision detection
- `paddle.py` - Paddle class for player and AI
- `ball.py` - Ball class with movement and physics
- `scoreboard.py` - Score display
