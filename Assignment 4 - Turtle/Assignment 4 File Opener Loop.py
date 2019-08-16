import turtle
import csv

master_list = []


open1 = True
while open1 == True:
    
    user_file = input('Enter file to open and draw:')
    if user_file == 'Quit':
        open1 = False

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

    
        f.close()
        
        

    except FileNotFoundError:
        print('Could not open file :', user_file)
        

