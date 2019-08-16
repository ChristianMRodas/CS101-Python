

#Trial 2

game_board_row1 = ['A','B','C','D']
game_board_row2 = ['E','F','F','E']
game_board_row3 = ['D','C','B','A']

main = []
main.append(game_board_row1)
main.append(game_board_row2)
main.append(game_board_row3)

print(main)
# print(main[1][1])

user_board = [['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*']]
hidden_board = [['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*']]
 
print("user",user_board)


#First user guess
user_guess_y = int(input("What row?:"))
print(user_guess_y)

user_guess_x = int(input("What column?:"))
print(user_guess_x)

print(main[user_guess_y][user_guess_x])



#Saves the value guessed of main board
first_value_holder = main[user_guess_y][user_guess_x]
print("This is the value for first guess", first_value_holder)



#Replaces the index value with another value
#main[user_guess_y][user_guess_x]= "P"
#print(main[user_guess_y][user_guess_x])


print("main",main)

print()
#Now lets try with a hidden board
print("user",user_board)



#Take previous input and "flip" value so,
flipped_board = user_board
print("flipped", flipped_board)

#EROR
print("user board,", user_board)

flipped_board[user_guess_y][user_guess_x] = main[user_guess_y][user_guess_x]

print("flipped after first guess",flipped_board)




print()


#Next lets flip 2nd value
user_guess_y2 = int(input("2What row?:"))
print(user_guess_y2)
#user while if y1 = y2 to repeat the above print statement

user_guess_x2 = int(input("2What column?:"))
print(user_guess_x2)



#Saves the value guessed of main board
second_value_holder = main[user_guess_y2][user_guess_x2]
print("This is the value for second guess", second_value_holder)

flipped_board[user_guess_y2][user_guess_x2] = main[user_guess_y2][user_guess_x2]
print("flipped",flipped_board)



# Next step is check if the 2 cards/ values are the same
# if not then the board is reset back to the hidden board
if first_value_holder != second_value_holder:
    print("Values are NOT the same, so values hide")

    user_board = hidden_board
    flipped_board = user_board


if first_value_holder == second_value_holder:
    print("Both values are the same")

    #Now the hidden board, will premamntly show the two equal values





print("main board",main)
print("user",user_board)
print("flipped",flipped_board)

    #I think above will work, but it may loose old value pairs ie 2 equal cards/values



#For game over
if main == user_board:
    print("Congrats all pairs found")


#For making it look like the pdf/exapmle board,
#just use a for loop to iterate for every row, then print()
#for the next row







print()
print(main)
main.append('J')
print(main)



