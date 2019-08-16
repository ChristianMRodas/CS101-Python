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
while i < 600:
    x = [i,0,i+10,10]
    grid2.append(x)
    i +=10
    
i = 0
while i < 600:
    x2 =[i,10,i+10,200]
    grid2.append(x2)
    i += 10
print(grid2)

i = 0
k = 0
while k < 600:
    y = [i,k,i+10,k+10]
    grid.append(y)
    i = 0
    while i < 590:
        i += 10
        x = [i,k,i+10,k+10]
        grid.append(x)
        
    k += 10

print(grid)
print(len(grid))
    
    
    
        
