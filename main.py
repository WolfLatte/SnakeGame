import tkinter as tk

# Game Settings
ROWS = 50
COLUMNS = 50
SPACE = 25
WINDOW_WIDTH = SPACE * COLUMNS
WINDOW_HEIGHT = SPACE * ROWS

BODY = 1
SNAKE_COLOR = "green"
FOOD_COLOR = "purple"
BG = "white"

class Snake:
    def __init__(self):
        self.coordinates = [(COLUMNS//2, ROWS//2)]
        self.direction = 'Right'

    def move(self):
        x, y = self.coordinates[0]
        if self.direction == 'Right':
            x += 1
        elif self.direction == 'Left':
            x -= 1
        elif self.direction == 'Up':
            y -= 1
        elif self.direction == 'Down':
            y += 1
        self.coordinates.insert(0, (x, y))

    def turn(self, direction):
        if direction == 'Right' and self.direction!= 'Left':
            self.direction = direction
        elif direction== 'Left' and self.direction!= 'Right':
            self.direction = direction
        elif direction == 'Up' and self.direction!= 'Down':
            self.direction = direction
        elif direction == 'Down' and self.direction!= 'Up':
            self.direction = direction

    def check_collision(self):
        x, y = self.coordinates[0]
        if x < 0 or x >= COLUMNS or y < 0 or y >= ROWS:
            return True
        for i in range(1, len(self.coordinates)):
            if self.coordinates[i] == self.coordinates[0]:
                return True
        return False

class Food:
    def __init__(self):
        self.coordinates = (COLUMNS//2, ROWS//2)

    def move(self):
        x, y = self.coordinates
        dx, dy = 0, 0
        while dx == 0 and dy == 0:
            dx, dy = random.choice([-1, 1]), random.choice([-1, 1])
        self.coordinates = (x + dx, y + dy)

def game_over():
    window.quit()

def update_score(score):
    

def draw_snake(snake, canvas):
    canvas.delete("snake")
    for x, y in snake.coordinates:
        canvas.create_rectangle(x*SPACE, y*SPACE, (x+1)*SPACE, (y+1)*SPACE, fill=SNAKE_COLOR, tag="snake")

def draw_food(food, canvas):
    canvas.delete("food")
    x, y = food.coordinates
    canvas.create_rectangle(x*SPACE, y*SPACE, (x+1)*SPACE, (y+1)*SPACE, fill=FOOD_COLOR, tag="food")
