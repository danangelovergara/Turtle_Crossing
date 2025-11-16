from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
    
    def paddle_hit(self):
        """Increase speed slightly when paddle hits the ball"""
        self.x_move *= -1
        # Increase speed by 10% each hit (up to a max of 20 for safety)
        if abs(self.x_move) < 20:
            self.x_move *= 1.1
    
    def reset_position(self):
        """Reset ball to center with random direction"""
        self.goto(0, 0)
        self.x_move = 10 if random.random() > 0.5 else -10
        self.y_move = random.randint(-10, 10)
        if self.y_move == 0:
            self.y_move = 5


