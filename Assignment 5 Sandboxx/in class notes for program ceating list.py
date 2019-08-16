#for program you can use a list of lists or dictionary. In like a grid pattern.
#then you can move it up down on the list or right or left.
#for material he has it tuples so stone at 0,0 then next is
#i]maybe not tuple

#so back to top, to mvoe it up or dwon, it goes based off the grid.
#then it checks if something is in the list. if no then moves it into in the
#the spot.
#how do you every cyc
#          update screen from backwards

#000000
#000100
#000000

#the 1 is the sand n 0 is empty

# [ [0,0],[0,0][0,0]}
#'            '
#'              '


#grd = [ [0,0],[0,0][0,0]} ]

#for cnt in range(4):
#   row.append(0)

#- [0,0,0,0]

#then another loop
# for grid = []
#for cnt in range(4):
    #grd.append(row)

#- it prints 4,4 0's

#so we ought to copy it usnig .copy

#for cnt in range(4):
#   grd.append(row.copy()

#for row in range(4):
#   ROW[]
#   for col in range(4):
#       row.append(0)

#    grid.append(row)


def draw_stone (block_type,x,y):
                x2 = x + 10
                y2 = y + 10
                win.draw_rect(x,x2,y,y2,'Gray')

#Creating Gird 6x6
    
    for cnt in range(6):
        x = (0,0,0,0,0,0)
        grid.append(x)
    print(grid)

grid.append(lower_right_cord)
grid.append(upper_left_cord)
grid.append(block_type)

#iterating list
    num_grid = len(grid)
    print(grid)

    i = 0
    k = 0
    while i < 10 and num_grid > 0:
        print(grid[i][k])
        i += 1
        k += 1
