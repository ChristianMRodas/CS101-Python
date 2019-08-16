##CS 101
##Program 5
##Spring 2018
##
##Christian Rodas
##cmrnmc@mail.umkc.edu
##
##PROGRAM: Creating simple blocks onto Sandbox
##  The program will be able to convert user input from a pixel input to block output 
##  on the sandbox. Rocks float, sand goes down until it hits another block, then it
##  stays in place. Water is same as sand only once it hits another block, it moves
##  left to right randomly.
##    
##ALGORITHM:
##    1. Import Modules gravity, random, time
##    2. Create the sandbox window and size
##    3. Start list that will hold elements
##    4. Function for draw blocks.
##    5 Start the program
##    6 Get user input
##    7 Clears screen when button is pressed
##    8 Converts pixels to blocks and prevents box overlapping or uneven blocks
##    9 Call draw function after conversion
##    10 Keeps drawings on sandbox
##    11 Checks type of block and stops block from going over the screen
##    12 Determines if there is a block under it and stops block from moving down
##    13 If block is water, move water left or right
##    14 Prints updated blocks ie sand and water
##    15 Sends user farewell message if sandbox is closed
##
##Error Handling: 
##
##Other Comments: 
##
##################################################################################


#Import Mods
import gravity_mod as gfx
import random
import time

# Creates a window 100 wide, and 100 tall
win = gfx.GravWindow("Sandbox")


start = time.time()
time.sleep(.25)
end = time.time()

# Empty List for events
grid = []

# Function for drawing blocks
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

    grid.append(block_data)
    
# Starts the program
while True:
    try:
        win.draw_screen()
        time.sleep(.1)

# Gets user input from sandbox
        events = win.get_events()

# Clears screen
        if events == ['CLEAR']:
            win.draw_screen()

# Starts converting pixels to blocks once an event has started
        num_events = len(events)
        if num_events >= 1 and events != ['CLEAR']:
    
            block_type = events[0][0]
            
#For x cord
            upper_left_cord = events[0][1]
        
            x10 = upper_left_cord % 10

            upper_left_cord = upper_left_cord - x10

        
#For y cord
            lower_right_cord = events[0][2]
 
            y10 = lower_right_cord % 10
        
            lower_right_cord = lower_right_cord - y10

# Calls Function after pixels have been converted to blocks and block type
            draw_stone(upper_left_cord, lower_right_cord, block_type)

# Keeps drawings on sandbox
        total_items = 0
        for items in (grid):

            one = items[0]
            two = items[1]
            three = items[2]
            four = items[3]
            five = items[4]

# Checks type of block and stops block from going over the screen
            if five == 'Tan' and four < 600:

                down_y1 = two + 10
                down_y2 = four + 10

# Determines if there is a block under it and stops block from moving
                all_items = 0
                while all_items < total_items:

                    if (grid[all_items][0:4]) == items[0:4]:
                        two = two -10
                        four = four -10
                        new_item = one,two,three,four,five

                    if (grid[all_items][0:4]) != items[0:4]:
                        new_item = one,down_y1,three,down_y2,five

                    all_items += 1

                grid.remove(items)
                items = new_item
                grid.append(items)


# Water's attribute
            if five == 'Blue' and four < 600:

                two = two + 10
                four = four + 10

                all_items = 0
                while all_items < total_items:

                    if (grid[all_items][0:4]) == items[0:4]:
                        two = two -10
                        four = four -10
                        
# Randomly chooses to go left or right
                        random_direction = random.randrange(2)
                        if random_direction == 1 and 0 < three < 600:
                            one = one +10
                            three = three +10
                            new_item = one,two,three,four,five
                            
                        if random_direction != 1 and 0< three < 600:
                            one = one -10
                            three = three -10
                            new_item = one,two,three,four,five

                    if (grid[all_items][0:4]) != items[0:4]:
                        new_item = one,down_y1,three,down_y2,five

                    all_items += 1

                grid.remove(items)
                items = new_item
                grid.append(items)



# Prints updated blocks ie sand and water
            win.draw_rect(one,two,three,four,five)

            total_items += 1
 

# Catches if user closes window
    except _tkinter.TclError:
        print('Thanks for playing')
    except NameError:
        print('Thanks for playing')
        
        
        
