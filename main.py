import tkinter as tk

# Game Settings
ROWS = 25
COLUMNS = 25
SPACE = 25
WINDOW_WIDTH = SPACE * COLUMNS
WINDOW_HEIGHT = SPACE * ROWS


BODY = 1
SNAKE_COLOR = "E7906D"
FOOD = "#996DE7"
BG = "white"


#Base funtions

class Snake:
    pass


class Food:
    pass


def turn():
    pass


def change_direction(turn):
    pass

def game_over():
    pass


#######################################################
window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas =tk.Canvas(
    window,
    bg=BG,
    width=WINDOW_WIDTH,
    height=WINDOW_HEIGHT,
    borderwidth=0,
    highlightthickness=0
)
canvas.pack()

score=0
label1=Label(master=window, text="Points:{}".format(score), font=('consolas',20))
label1.pack()

window.mainloop()