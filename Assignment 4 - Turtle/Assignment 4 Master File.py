##CS 101
##Program 4
##Spring 2018
##
##Christian Rodas
##cmrnmc@mail.umkc.edu
##
##PROGRAM: Creating simple designs from files.
##  The program will be able to read a text file, convert it to a list and attribute
##  each object to a parameter on a function which outputs it to a design on turtle.
##
##    
##ALGORITHM:
##    1. Import Modules CSV and Turtle
##    2. Create functions to draw a circle, a line, and a rectangle on turtle, given specific parameters
##    3. Begin a loop for continous user input
##    4. Reset the turtle screen
##    5 Sets turtle for fastest drawing speed
##    6 Creates an empty list will hold all the text read from files.
##    7 Allows user to quit program
##    8 Read user file and check for errors
##    9 Seperate text from file into individual values
##    10 Append each and every row to the master list
##    11 Counts how many rows there are from the text file
##    12 Keep track of all values being added
##    13 Correct file text type so functions can read values
##    14 Determine which function to call
##    15 Each function call will verify that each value is the correct type for the function
##    16 If it is not callable, it will tell the user
##    17 Closes the file
##    18 This will tell user what is wrong with each file and what caused it.
##
##Error Handling: The pythonlogo 
##
##Other Comments: Turtle window is increased for easier visibility
##
##################################################################################


#1 Import modules
import turtle
import csv


#2 Functions

#Circle Function
def draw_circle (x : int,y : int,radius : int, color : str):
    turtle.pu()
    

    turtle.setx(x)
    turtle.sety(y)
    turtle.pd()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()
    turtle.ht() #This hides the turtle when circle is finished.


#Rectangle Function
def draw_rect (x : int,y : int, length : int, width: int, color : str):
    turtle.pu()
    turtle.goto(0,0)
    

    
    turtle.setx(x)
    turtle.sety(y)
    turtle.pd()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.width(width)

    turtle.pencolor(color)
    
    turtle.fd(length)
    turtle.end_fill()
    turtle.ht() #This hides the turtle when rectangle is finished.




#Line Function
def draw_lines (x : int,y : int, angle : int, length: int, color : str):
    turtle.pu()
    turtle.goto(0,0)
    
    turtle.setx(x)
    turtle.sety(y)
    turtle.pd()
    turtle.width(1)

    turtle.pencolor(color)
    turtle.seth(angle)
    turtle.fd(length)
    turtle.ht() #This hides the turtle when lines is finished.

 

# This setups of the window size for thr turtle, so it's easier to see.
turtle.setup(width=1250, height=650, startx=0, starty=0)

#3 This begins the loop for continous user input
open1 = True
while open1 == True:

    #Asks user for input
    user_file = input('Enter file to open and draw:')
    #4 Resets turtle screen everytime new input is given
    turtle.reset()

    #5 Sets turtle for fastest drawing speed
    turtle.speed(0)

    #6 Creates an empty list will hold all the text read from files.
    #It will clear when new input is given
    master_list = []

    #7 This will stop program when user enters quit
    if user_file == 'quit':
        open1 = False
        turtle.done()

    #8 This will begin to open and read user file and check for errors
    try:
        f = open(user_file)

    
        with open(user_file, 'r') as csvfile:
            #9 This will seperate text at every comma
            shapes = csv.reader(csvfile, delimiter =',')

            #10 This will append each and every row to the master list
            row_num = 1
            for row in shapes:
                
                master_list.append(row)
                row_num += 1

        # 11 This counts how many rows there are for the following loop
        num_rows = len(master_list)
    
        #Starts the index at 0,0
        i = 0
        i2 = 0
        while i < num_rows:
            x = len(master_list[i])
            #12 This to keep track of all values being added
            results = []



            #Second i Loop
            while i2 < x:
                current_section = (master_list[i][i2])
                results.append(current_section)

                i2 += 1
            

            i2 = 0
            i += 1

            # 13 corrects file text so functions can read values
            results = [space.strip(' ') for space in results]
            results = [case.lower() for case in results]
                
            # 14 This determines which function to call
            read_shape = results[0]
            
        #15 Each function call will verify that each value is the correct type for the function
            #Call Circle Function
            if read_shape == 'circle':
               
                a1 = int(results[1])
                a2 = int(results[2])
                a3 = int(results[3])
                a4 = str(results[4])
                
                draw_circle(a1,a2,a3,a4)

            #SCall Rectangle Function
            if read_shape == 'rect':
           
                r1 = int(results[1])
                r2 = int(results[2])
                r3 = int(results[3])
                r4 = int(results[4])
                r5 = str(results[5])
                
                draw_rect(r1,r2,r3,r4,r5)


            #Call Line Function
            if read_shape == 'line':
               
                r1 = int(results[1])
                r2 = int(results[2])
                r3 = int(results[3])
                r4 = int(results[4])
                r5 = str(results[5])
                
                draw_lines(r1,r2,r3,r4,r5)

            # 16 If it is not callable, it will tell the user
            if read_shape == 'triangle':
                print('Invalid shape')


        #Loop for drawing ends
                
        #17 Closes the file   
        f.close()
        
        
# 18 This will tell user what is wrong with each file and what caused it.
    except FileNotFoundError:
        print('Could not open file :', user_file)

    except ValueError:
        print()
        print('Could not convert an argument to int')
        print(results,'k')

    except IndexError:
        print('The line did not have proper number of arguments.')
        print(results,'k')








    
