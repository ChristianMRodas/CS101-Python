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

while True:
    # Draw on the screen
    win.draw_screen()

#Shows what was pressed
    one = win.get_events()
    print(one)
    print()
    
#Slow down time
    time.sleep(.5)
        
# Function for blocks n cord
    def draw_stone (x,y,block):
        x2 = upper_left_cord + 25
        y2 = lower_right_cord + 25
        print(x,x2,y,y2,block_type)

        if block_type == 'STONE':
            block_color = 'Gray'
            
        if block_type == 'SAND':
            block_color = 'Tan'
            
        if block_type == 'WATER':
            block_color = 'Blue'
            
        win.draw_rect(x,y,x2,y2,block_color)
        block_data = x,y,x2,y2,block_color
        print(block_data)
        grid.append(block_data)
        
        
#Function for sand to move down
       
                print(y)
        y = y +10
        print(y)
        y2 = y +10


#Take events and output something
    nums = len(one)
    if nums >= 1:
        input_list = []
        

        block_type = one[0][0]
        print('This is the block type', block_type)

        upper_left_cord = one[0][1]
        print('This the upper left corner', upper_left_cord)

        lower_right_cord = one[0][2]
        print('This the lower right corner', lower_right_cord)

  
        draw_stone(upper_left_cord, lower_right_cord, block_type)

#Iterates for every element
    i = 0
    k = 0
    grid_size = len(grid)
    print('This is the gird size', grid_size)
    while i <= grid_size and grid_size >= 1:
        print('Current num', i)
        print('The current set', grid[i])
        
        i += 1


    print(grid)
    
    
