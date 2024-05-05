import tkinter as tk
from tkinter import colorchooser
import random

# Create the game window
window = tk.Tk()

class Snake:
    def __init__(self, master):
        self.master = master
        master.title("Snake")


        # Set up the game canvas
        self.canvas = tk.Canvas(
            master, 
            width=400, 
            height=400, 
            bg='light green'
        )
        self.canvas.pack()


        # Create the snake and food
        self.snake = [(200, 200), (190, 200), (180, 200)]
        self.food = self.create_food()


        # Set up the game loop
        self.direction = 'Right'
        self.game_over = False
        self.delay = 200
        self.score = 0


        # Create the label for points
        self.label = tk.Label(
            master, 
            text=f"Points: {self.score}",
            font=('consolas',20)
        )
        self.label.pack()


        # Create the restart button
        self.restart_button = tk.Button(
            master=window, 
            text="Restart", 
            font=('consolas', 20), 
            command=self.game_restart
        )
        self.restart_button.pack()


        # Countdown timer label
        self.timer_label = tk.Label(
            master,
            text="",
            font=('consolas', 20)
        )
        self.timer_label.pack()


        # Bind arrow keys to change direction
        master.bind('<Up>', self.change_direction_up)
        master.bind('<Down>', self.change_direction_down)
        master.bind('<Left>', self.change_direction_left)
        master.bind('<Right>', self.change_direction_right)


        # Start the countdown timer
        self.countdown(3)


    def create_food(self):
        # Create a new piece of food at a random location on the canvas
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20
        food = self.canvas.create_oval(x, y, x+20, y+20, fill='purple')
        return food


    def draw_snake(self):
        self.square_size = 20
        self.canvas.delete('snake')


        for i, (x, y) in enumerate(self.snake):
            if i == 0:
                self.canvas.create_rectangle(x, y, x + self.square_size, y + self.square_size,
                                            fill='white', tags='snake')
            else:
                self.canvas.create_rectangle(x, y, x + self.square_size, y + self.square_size,
                                            fill='green', tags='snake')


    def move_snake(self):
        # Move the snake one step in the current direction
        head = self.snake[0]
        if self.direction == 'Up':
            new_head = (head[0], head[1]-20)
        elif self.direction == 'Down':
            new_head = (head[0], head[1]+20)
        elif self.direction == 'Left':
            new_head = (head[0]-20, head[1])
        elif self.direction == 'Right':
            new_head = (head[0]+20, head[1])
        self.snake.insert(0, new_head)
        self.canvas.delete(self.snake[-1])
        self.snake.pop()


    def check_collision(self):
        # Check for collision with the walls or the snake's body
        head = self.snake[0]
        if head[0] < 0 or head[0] >= 400 or head[1] < 0 or head[1] >= 400:
            self.game_over = True
        for segment in self.snake[1:]:
            if head == segment:
                self.game_over = True


    def game_restart(self):
        # Reset the game state
        self.canvas.delete("all")
        self.canvas.delete("You Lost")
        self.snake = [(200,200),(190,200),(180,200)]
        self.food = self.create_food()
        self.direction = 'Right'
        self.game_over = False
        self.delay = 100
        self.score = 0
        self.label.config(text="Score:{}".format(self.score))


        # Start the game loop
        self.game_loop()


    def check_food(self):
        # Check if the snake has eaten the food
        head_coords = self.canvas.coords(self.food)
        if self.snake[0][0] == int(head_coords[0]) and self.snake[0][1] == int(head_coords[1]):
            self.canvas.delete(self.food)
            self.food = self.create_food()
            self.score += 1
            self.label.config(text=f"Score: {self.score}")
            self.snake.append(self.snake[-1])


    def change_direction_up(self, event):
        if self.direction != 'Down':
            self.direction = 'Up'


    def change_direction_down(self, event):
        if self.direction != 'Up':
            self.direction = 'Down'


    def change_direction_left(self, event):
        if self.direction != 'Right':
            self.direction = 'Left'


    def change_direction_right(self, event):
        if self.direction != 'Left':
            self.direction = 'Right'


    def game_loop(self):
        # Main game loop
        if not self.game_over:
            self.draw_snake()
            self.move_snake()
            self.check_collision()
            self.check_food()
            if not self.game_over:
                self.master.after(self.delay, self.game_loop)
            else:
                self.canvas.delete("all")
                self.canvas.create_text(
                    200, 
                    200, 
                    text="You Lost", 
                    fill='white', 
                    font=('consolas',30)
                )


    def countdown(self, count):
        # Countdown timer
        self.timer_label.config(text=f"Game starting in {count} seconds...")
        if count > 0:
            self.master.after(1000, self.countdown, count - 1)
        else:
            self.timer_label.pack_forget()
            self.game_loop()


    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose color")
        if color_code[1]:  
            new_color = color_code[1]  
            self.canvas.config(bg=new_color)  


# Create the Snake game instance
snake_game = Snake(window)

# Create the color button
color_button = tk.Button(window, text="Select Background Color", command=snake_game.choose_color)
color_button.pack()

# Run the game window
window.mainloop()