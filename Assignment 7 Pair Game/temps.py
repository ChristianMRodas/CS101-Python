import random

def flip (card):
    

    if card == 2:

        return card
    if card != 2:

        return "Incorrect"


def creates_board (difficulty):
    if difficulty == 2:
        print(" 1 2 3 4")
    i = 0
    while i < 5:
        i = i + 1
        print(("   %d") % i ,end='')
    print()
    i = 0
    while i < 5:
        i += 1
        print(("%d|") % i)
    return None


def board_2 (difficulty):
    width = difficulty
    height = difficulty
    game_board = []
    row = []
    letters2 = "ABCDEFGHIJk"


    
    hidden_icon = 0
    #FIXME symbol should be  *

    
    for i in range(width):
        hidden_icon = random.choice(letters2)
        row.append(hidden_icon)


    for i in range(height):
        game_board.append(row)
        

    print(game_board)

#Finds specific Value from Game Board
    for rows in game_board:
        for values in rows:
            print(values)
            if values == "H":
                print('Found H')

    return game_board



x = creates_board(2)
print(x)


user_guess = int(input("guess a num:"))


x = flip(user_guess)


y = board_2(user_guess)
print(y)


# Solved picking random letters 
letters = "ABCDEFGHIJk"
test = random.choice(letters)
print(test)


# I tried to find a single value in a nested loop but failed
##print(trial[2])

while x == "Incorrect":
    user_guess = int(input("guess a num:"))


    x = flip(user_guess)

print(x)
    





game_board = [['A','B','C','D'],['E','F','F','E'],['D','C','B','A']]
print(game_board)

game_board = [['A','*','C','D'],['E','F','F','E'],['D','C','B','A']]
print(game_board)

user_letter = str(input("Guess a letter:"))


if user_letter == "B":
    game_board = [['A','B','C','D'],['E','F','F','E'],['D','C','B','A']]

    print(game_board)


print(game_board[1:0])




