import turtle
import csv

user_file = input('Enter file to open and draw:')


master_list = []

try:
    f = open(user_file)

    with open(user_file, 'r') as csvfile:
        shapes = csv.reader(csvfile, delimiter =',')

        row_num = 1
        for row in shapes:
            print('Row #%d:' % row_num, row)
            master_list.append(row)
            row_num += 1
        print()
    
    print(master_list[1][4])
    print()

    num_rows = len(master_list)
    print(num_rows)
    print()
    

    


    i = 0
    i2 = 0
    while i < 2:
        x = len(master_list[i])
        print(x)
        while i2 < x:
            print(master_list[i][i2])
            
            i2 += 1
        print()
        print('Next row')
        i2 = 0
        i += 1

    
    f.close()

except FileNotFoundError:
    print('Could not open file :', user_file)
