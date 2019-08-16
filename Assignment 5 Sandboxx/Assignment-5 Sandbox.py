import gravity_mod as gfx

import random

# Creates a window 100 wide, and 100 tall
win = gfx.GravWindow("Sandbox")
# Draw on the screen

win.draw_screen()

import time
start = time.time()
print("Before sleep")
time.sleep(.25)
end = time.time()
print("The program slept for ", end - start, "seconds")

grid = []

while True:
    win.draw_screen()

#Shows what was pressed
    one = win.get_events()
    print(one)

    x = type(one)


    
#Slow down time
    time.sleep(.1)
        
#Creates Blocks
    win.draw_rect(0,0,25,25,'Gray')

    win.draw_rect(25,25,50,50,'Tan')

    win.draw_rect(50,50,75,75,'Blue')

    win.draw_rect(575,575,600,600,'Gray')

# Function for blocks n cord
    def draw_stone (block_type, upper_left_cord, lower_right_cord):
        x2 = upper_left_cord + 10
        y2 = lower_right_cord + 10
        win.draw_rect(upper_left_cord,x2,lower_right_cord,y2,block_type)



#Take events and output something
    nums = len(one)
    print(nums)
    if nums >= 1:
        input_list = []
        win.draw_screen()
        print('yes')

        
        block_type = one[0][0]
        input_list.append(block_type)
        print(block_type)

        upper_left_cord = one[0][1]
        input_list.append(upper_left_cord)
        print('This the upper left corner', upper_left_cord)

        lower_right_cord = one[0][2]
        input_list.append(lower_right_cord)
        print('This the lower right corner', lower_right_cord)

 

        


        if block_type == 'STONE':
            print('Printing stone')
            win.draw_rect(150,150,200,200,'Gray')

            draw_stone


        if block_type == 'SAND':
            print('Printing stone')
            win.draw_rect(250,250,300,300,'Tan')

        if block_type == 'WATER':
            print('Printing stone')
            win.draw_rect(400,30,350,350,'Blue')
 
        


        grid.append(input_list)


    win.draw_rect(510,510,500,500,'Tan')
    print(grid)

    
    

#increase the scrren by 6 
    
