import gravity_mod as gfx
import random

# Creates a window 100 wide, and 100 tall
win = gfx.GravWindow("Sandbox")

import time
start = time.time()
print("Before sleep")
time.sleep(.25)
end = time.time()
print("The program slept for ", end - start, "seconds")

grid = []

# Function for blocks n cord
def draw_stone (x,y,block):
    x2 = upper_left_cord + 10
    y2 = lower_right_cord + 10
    print(x,x2,y,y2,block_type)

    if block_type == 'STONE':
        block_color = 'Gray'
            
    if block_type == 'SAND':
        block_color = 'Tan'

        
            
    if block_type == 'WATER':
        block_color = 'Blue'
            
    win.draw_rect(x,y,x2,y2,block_color)
    block_data = x,y,x2,y2,block_color
    print('This is the block data', block_data)
    grid.append(block_data)
    

while True:
    try:
        print()
        print('New event')
        win.draw_screen()
        time.sleep(.4)
        events = win.get_events()
        print('What user clicked on', events)

        if events == ['CLEAR']:
            print('clear the sceen')
            win.draw_screen()
            
        num_events = len(events)
        if num_events >= 1 and events != ['CLEAR']:
    
            block_type = events[0][0]
            print('This is the block type', block_type)
            
    except _tkinter.TclError:
        print('Thanks for playing')
    except NameError:
        print('Thanks for playing')
