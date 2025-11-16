# replay.py
import time
from turtle import Turtle

def show_play_again(screen, prompt_y=-80, btn_y=-140):
    """
    Draw a Play-again UI and return True (YES) or False (NO).
    Uses a single screen click handler and a small polling loop to wait
    for the player's choice. Does not execv or close the window itself.
    """

    # background box
    bg = Turtle()
    bg.hideturtle()
    bg.penup()
    bg.speed("fastest")
    left = -180
    right = 180
    top = prompt_y + 40
    bottom = btn_y - 40
    bg.goto(left, top)
    bg.color("black")
    bg.fillcolor("gray10")
    bg.begin_fill()
    bg.pendown()
    bg.goto(right, top)
    bg.goto(right, bottom)
    bg.goto(left, bottom)
    bg.goto(left, top)
    bg.end_fill()
    bg.penup()

    # prompt text
    prompt = Turtle()
    prompt.hideturtle()
    prompt.penup()
    prompt.color("white")
    prompt.goto(0, prompt_y)
    prompt.write("Play again?", align="center", font=("Arial", 22, "bold"))

    # YES button (green)
    yes_x, yes_y = -80, btn_y
    yes_btn = Turtle("square")
    yes_btn.hideturtle()
    yes_btn.penup()
    yes_btn.color("green")
    yes_btn.shapesize(stretch_wid=1.4, stretch_len=3)
    yes_btn.goto(yes_x, yes_y)
    yes_btn.showturtle()

    yes_label = Turtle()
    yes_label.hideturtle()
    yes_label.penup()
    yes_label.color("black")
    yes_label.goto(yes_x, yes_y - 6)
    yes_label.write("YES", align="center", font=("Arial", 14, "bold"))

    # NO button (red)
    no_x, no_y = 80, btn_y
    no_btn = Turtle("square")
    no_btn.hideturtle()
    no_btn.penup()
    no_btn.color("red")
    no_btn.shapesize(stretch_wid=1.4, stretch_len=3)
    no_btn.goto(no_x, no_y)
    no_btn.showturtle()

    no_label = Turtle()
    no_label.hideturtle()
    no_label.penup()
    no_label.color("black")
    no_label.goto(no_x, no_y - 6)
    no_label.write("NO", align="center", font=("Arial", 14, "bold"))

    # approximate button rectangles (px)
    btn_half_w = 3 * 10
    btn_half_h = 1.4 * 10
    yes_rect = (yes_x - btn_half_w, yes_y - btn_half_h, yes_x + btn_half_w, yes_y + btn_half_h)
    no_rect = (no_x - btn_half_w, no_y - btn_half_h, no_x + btn_half_w, no_y + btn_half_h)

    chosen = {"val": None}

    def cleanup():
        try:
            screen.onscreenclick(None)
        except Exception:
            pass
        for t in (bg, prompt, yes_btn, no_btn, yes_label, no_label):
            try:
                t.clear()
                t.hideturtle()
                t.penup()
                t.goto(10000, 10000)
            except Exception:
                pass

    def in_rect(x, y, rect):
        x1, y1, x2, y2 = rect
        return x1 <= x <= x2 and y1 <= y <= y2

    def handle_click(x, y):
        # Decide if click was inside yes or no button
        if in_rect(x, y, yes_rect):
            chosen["val"] = True
            cleanup()
        elif in_rect(x, y, no_rect):
            chosen["val"] = False
            cleanup()

    screen.onscreenclick(handle_click)
    screen.update()

    # wait until the user clicks one of the buttons (polling loop)
    while chosen["val"] is None:
        try:
            screen.update()
        except Exception:
            # if the screen is in a bad state, return False to quit
            cleanup()
            return False
        time.sleep(0.05)

    return bool(chosen["val"])