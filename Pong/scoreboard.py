from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.ai_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # Left side - Player score
        self.goto(-100, 260)
        self.write(f"{self.player_score}", align="center", font=("Courier", 24, "normal"))
        # Center line
        self.goto(0, 260)
        self.write("|", align="center", font=("Courier", 24, "normal"))
        # Right side - AI score
        self.goto(100, 260)
        self.write(f"{self.ai_score}", align="center", font=("Courier", 24, "normal"))

    def increase_player_score(self):
        self.player_score += 1
        self.update_scoreboard()
    
    def increase_ai_score(self):
        self.ai_score += 1
        self.update_scoreboard()