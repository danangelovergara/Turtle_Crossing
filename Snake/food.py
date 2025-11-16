from turtle import Turtle
import random

GRID_SIZE = 20
MAX_INDEX = 14  # GRID_SIZE * MAX_INDEX = 280 (board boundary)

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # keep food smaller than a cell so it's centered inside the box
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("red")
        self.speed("fastest")
        # initial placement
        self.refresh()

    def refresh(self, occupied_positions=None):
        # pick a random grid-aligned cell
        while True:
            random_x = random.randint(-MAX_INDEX, MAX_INDEX) * GRID_SIZE
            random_y = random.randint(-MAX_INDEX, MAX_INDEX) * GRID_SIZE
            if occupied_positions and (random_x, random_y) in occupied_positions:
                continue
            self.goto(random_x, random_y)
            break