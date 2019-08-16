########################################################################
##
## CS 101
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import gravity_mod as gfx
import time
import random

# Set constants for screen size, block size, etc.
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BLOCK_SIZE = 10
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

ROCK_COLOR = "Gray"
SAND_COLOR = "Tan"
WATER_COLOR = "Blue"

def create_grid(width = GRID_WIDTH, height = GRID_HEIGHT):
    """ Create new blank grid """
    return [ [None for col in range(GRID_WIDTH)] for row in range(GRID_HEIGHT)]

    
def get_grid_coords(pixel_x, pixel_y):
    """ Returns an X, Y that has been adjusted to the block grid """
    return pixel_x // BLOCK_SIZE, pixel_y // BLOCK_SIZE


def get_screen_coords(x, y):
    """ returns x y on actual screen coordinates translated from grid coordinates. """
    return x * BLOCK_SIZE, y * BLOCK_SIZE


def draw_grid(play_grid, win):
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if play_grid[row][col] is not None:
                x, y = get_screen_coords(col, row)
                win.draw_rect(x, y, x + BLOCK_SIZE, y + BLOCK_SIZE, play_grid[row][col])


def process_events(play_grid):
    for command in events:
        if command == "CLEAR":
            clear_grid(play_grid)
        else:
            item, x, y = command
            block_x, block_y = get_grid_coords(x, y)
            if block_x < GRID_WIDTH and block_y < GRID_HEIGHT and play_grid[block_y][block_x] is None:
                if item == "STONE":
                    play_grid[block_y][block_x] = ROCK_COLOR
                elif item == "SAND":
                    play_grid[block_y][block_x] = SAND_COLOR
                else:
                    play_grid[block_y][block_x] = WATER_COLOR


def clear_grid(play_grid):
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            play_grid[row][col] = None


def update_game(play_grid):
    row = GRID_HEIGHT - 1
    while row >= 0:
        cols = [cnt for cnt in range(GRID_WIDTH)]
        while len(cols) > 0:
            col = random.choice(cols)
            if play_grid[row][col] is not None:
                color = play_grid[row][col]
                if color == SAND_COLOR:
                    if row < GRID_HEIGHT - 1:
                        if play_grid[row + 1][col] is None:
                            play_grid[row + 1][col] = color
                            play_grid[row][col] = None
                        elif play_grid[row + 1][col] == WATER_COLOR:
                            play_grid[row + 1][col] = color
                            play_grid[row][col] = WATER_COLOR
                elif color == WATER_COLOR:
                    if row < GRID_HEIGHT - 1 and play_grid[row + 1][col] is None:
                        play_grid[row + 1][col] = color
                        play_grid[row][col] = None
                    else:  # random of both sides to slosh into.
                        choices = []
                        if col > 0 and play_grid[row][col - 1] is None:
                            choices.append((row, col - 1))
                        if col < GRID_WIDTH - 1 and play_grid[row][col + 1] is None:
                            choices.append((row, col + 1))
                        if len(choices) > 0:
                            ch = random.randint(0, len(choices) - 1)
                            new_row, new_col = choices[ch]
                            play_grid[new_row][new_col] = play_grid[row][col]
                            play_grid[row][col] = None
                            # if new_col > col:
                            #    col = col + 1
            cols.remove(col)
        row = row - 1


win = gfx.GravWindow("Python Sandbox")
grid = create_grid()

while True:

    events = win.get_events()
    if len(events) > 0:
        process_events(grid)

    update_game(grid)

    draw_grid(grid, win)

    win.draw_screen()
