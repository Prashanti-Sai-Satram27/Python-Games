import tkinter as tk
import random

# Constants
WIDTH = 500
HEIGHT = 500
SPEED = 100 # Adjusted for a smoother game experience
SPACE_SIZE = 50
BODY_SIZE = 3
SNAKE_COLOR = "red"
FOOD_COLOR = "white"
BACKGROUND_COLOR = "black"

# Snake class to manage the snake's properties and behavior
class Snake:
    def __init__(self):
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_SIZE):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

# Food class to manage the food's properties and behavior
class Food:
    def __init__(self):
        x = random.randint(0, int(WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# Function to manage the snake's next move
def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Points:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

# Function to change the snake's direction
def change_direction(new_direction):
    global direction
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

# Function to check for collisions
def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False

# Function to display the game over message
def game_over():
    canvas.delete("all")
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")

# Set up the main window
window = tk.Tk()
window.title("Snake Game")

# Score and direction
score = 0
direction = 'down'

# Display the score
label = tk.Label(window, text="Points:{}".format(score), font=('consolas', 20))
label.pack()

# Create the canvas for the game
canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
canvas.pack()

window.update()

# Center the window on the screen
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Bind the arrow keys to change direction
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Create snake and food objects
snake = Snake()
food = Food()

# Start the game loop
next_turn(snake, food)

# Run the main loop
window.mainloop()
