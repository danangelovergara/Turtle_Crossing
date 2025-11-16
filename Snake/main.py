from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from replay import show_play_again
import time

GRID_SIZE = 20
MAX_INDEX = 14  # GRID_SIZE * MAX_INDEX = 280 (board boundary)
DRAW_GRID = True
SLEEP_TIME = 0.06

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

def draw_grid(grid_size=GRID_SIZE, max_index=MAX_INDEX):
    drawer = Turtle()
    drawer.hideturtle()
    drawer.speed("fastest")
    drawer.color("gray20")
    drawer.penup()
    # offset grid lines by half a cell so centers lie inside boxes
    start = -max_index * grid_size - (grid_size / 2)
    end = max_index * grid_size + (grid_size / 2)
    x = start
    while x <= end:
        drawer.goto(x, start)
        drawer.pendown()
        drawer.goto(x, end)
        drawer.penup()
        x += grid_size
    y = start
    while y <= end:
        drawer.goto(start, y)
        drawer.pendown()
        drawer.goto(end, y)
        drawer.penup()
        y += grid_size

def grid_round_to_cell(value, grid_size=GRID_SIZE):
    return round(value / grid_size) * grid_size

def occupied_cells_from_snake(snake):
    return {(grid_round_to_cell(seg.xcor()), grid_round_to_cell(seg.ycor())) for seg in snake.segments}

if DRAW_GRID:
    draw_grid()

# globals for current game objects (so we can clean them up on restart)
snake = None
food = None
scoreboard = None

def init_game_objects():
    global snake, food, scoreboard
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    # ensure first food spawn doesn't land on snake
    food.refresh(occupied_positions=occupied_cells_from_snake(snake))

def cleanup_game_objects():
    global snake, food, scoreboard
    # hide and remove snake segments
    if snake:
        for seg in snake.segments:
            try:
                seg.clear()
                seg.hideturtle()
                seg.penup()
                seg.goto(10000, 10000)
            except Exception:
                pass
    # remove food
    if food:
        try:
            food.clear()
            food.hideturtle()
            food.penup()
            food.goto(10000, 10000)
        except Exception:
            pass
    # remove scoreboard
    if scoreboard:
        try:
            scoreboard.clear()
            scoreboard.hideturtle()
            scoreboard.penup()
            scoreboard.goto(10000, 10000)
        except Exception:
            pass
    # reset globals
    snake = None
    food = None
    scoreboard = None

def run_game_once():
    """
    Initializes objects and runs a single game until it ends.
    Returns when the game ends (Game Over displayed).
    """
    init_game_objects()
    screen.listen()
    screen.onkey(lambda: snake.up(), "Up")
    screen.onkey(lambda: snake.down(), "Down")
    screen.onkey(lambda: snake.left(), "Left")
    screen.onkey(lambda: snake.right(), "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(SLEEP_TIME)
        snake.move()

        # Collision with food — compare grid indices to avoid float drift
        if (grid_round_to_cell(snake.head.xcor()) == grid_round_to_cell(food.xcor())
                and grid_round_to_cell(snake.head.ycor()) == grid_round_to_cell(food.ycor())):
            snake.extend()  # grow first so new occupied cell is included
            scoreboard.increase_score()
            # refresh while avoiding snake positions
            food.refresh(occupied_positions=occupied_cells_from_snake(snake))

        # Wall Collision
        if (snake.head.xcor() > 280 or snake.head.xcor() < -280
                or snake.head.ycor() > 280 or snake.head.ycor() < -280):
            game_is_on = False
            scoreboard.game_over()

        # Self Collision
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    # game over displayed; return to caller to ask for replay/cleanup
    return

def main_loop():
    """
    Run games until the player chooses not to replay.
    """
    while True:
        run_game_once()
        # show prompt, returns True if player chose YES, False if NO
        play_again = show_play_again(screen)
        if not play_again:
            break
        # clear previous game objects (grid is preserved)
        cleanup_game_objects()
    # final close
    try:
        screen.bye()
    except Exception:
        pass

if __name__ == "__main__":
    main_loop()