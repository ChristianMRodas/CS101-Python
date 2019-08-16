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
grid2 = []

# Function for blocks n cord
def draw_stone (x,y,block):
    x2 = i + 10
    y2 = i + 10
    print(x,x2,y,y2,block)

            
    win.draw_rect(x,y,x2,y2,block)
    block_data = x,y,x2,y2,block
    print('This is the block data', block_data)
    grid.append(block_data)
    

i = 0
k = 0
while k < 60:
    y = [i,k,i+10,k+10]
    grid.append(y)
    i = 0
    while i < 60:
        i += 10
        x = [i,k,i+10,k+10]
        grid.append(x)
        
    k += 10

print(grid)
print(len(grid))


while True:
    print()
    print('New event')
    win.draw_screen()
    time.sleep(.5)
    events = win.get_events()
    print('What user clicked on', events)

    
    num_events = len(events)
    if num_events >= 1:
    
        block_type = events[0][0]
        print('This is the block type', block_type)
#For x cord
        upper_left_cord = events[0][1]
        print('This the upper left corner', upper_left_cord)
        
        x10 = upper_left_cord % 10
        print('This is mod 10', x10)
        
        upper_left_cord = upper_left_cord - x10
        print('This is upper_left_cord round to a 10',upper_left_cord)
        print('This is mod 10', x10)
        
#For y cord
        lower_right_cord = events[0][2]
        print('This the lower right corner', lower_right_cord)

        y10 = lower_right_cord % 10
        print('This is mod 10', y10)
        
        lower_right_cord = lower_right_cord - y10
        print('This is lower_right_cord round to a 10', lower_right_cord)
        print('This is mod 10', y10)

  
        draw_stone(upper_left_cord, lower_right_cord, block_type)

    
    total_items = 0
    for items in (grid):
        print('These are the items in the grid',items)

        one = items[0]
        two = items[1]
        three = items[2]
        four = items[3]
        five = items[4]

        if five == 'Tan' and four < 600:

            two = two + 10

            four = four + 10

            grid.remove(items)
    
            items = one,two,three,four,five
            grid.append(items)
            

        win.draw_rect(one,two,three,four,five)

        total_items += 1
        print(total_items)

    

        

    print(grid)   
