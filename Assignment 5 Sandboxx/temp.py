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

        if events == 'CLEAR':
            print('clear the sceen')
            
        num_events = len(events)
        if num_events >= 1 and events != 'CLEAR':
    
            block_type = events[0][0]
            print('This is the block type', block_type)
#For x cord
            upper_left_cord = events[0][1]

        
            x10 = upper_left_cord % 10

        
            upper_left_cord = upper_left_cord - x10

        
#For y cord
            lower_right_cord = events[0][2]
 

            y10 = lower_right_cord % 10

        
            lower_right_cord = lower_right_cord - y10


  
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

                p = 0
                while p <= total_items:
                    print('current item adding',items)
                    print('over all grid',grid[p])
                    if items == grid[p]:
                        print('Same so stop block')
                        two = two - 10
                        four = four -10
                    p += 1

    
                grid.remove(items)
    
                items = one,two,three,four,five
                grid.append(items)
            
            if five == 'Blue' and four < 600:

                two = two + 10
                four = four + 10

                h = 0
                while h <= total_items:
                    print('current item adding',items)
                    print('over all grid',grid[h])
                    if items == grid[h]:
                        print('Same so stop block')
                        two = two - 10
                        four = four -10

                        random_direction = random.randrange(2)
                        if random_direction == 1 and three < 600:
                            one = one +10
                            three = three +10
                            print(one,three)
                        if random_direction != 1 and three < 600:
                            one = one -10
                            three = three -10
                            print('not one',one,three)
                    
  

                    h += 1
   

                
                grid.remove(items)
                print('before',items)
                items = one,two,three,four,five
                print('after',items)
                grid.append(items)



            win.draw_rect(one,two,three,four,five)

            total_items += 1
            print(total_items)

    

        

        print(grid)


    except _tkinter.TclError:
        print('Thanks for playing')
        
        
        
























        
