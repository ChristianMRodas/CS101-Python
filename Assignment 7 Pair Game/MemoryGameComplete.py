##CS 101
##Program 7
##Spring 2018
##
##Christian Rodas
##cmrnmc@mail.umkc.edu
##
##PROGRAM: Taking in text and finding the synoyms most closely accosiated with a word
##  The program will take in a file full text, then it will go through that text 
##  and try to find a synoym for that from a dictionary. 
##    
##ALGORITHM:
##    1. Import Modules string, random
##    2. Start the Cell Class
##    3. Create Cell Functions that checks for comparison, prints board, and flips values
##    4. First function is called to standardize and organize text
##    5. Create Board Class
##    6. Board Class- Creates board size for 3 difficulties and checks for valid input
##    7. Board Class- Prints out user's board
##    8. Asks user for first guess and validates
##    9. Asks user for second guess and validates
##    10. Temporarily holds the user guesses
##    11. Shows user guesses on the user board
##    12. If it matches, then the user board updates, if not, it reverts to previous board
##    13. Resets temporary board and guesses back to defualt
##    14. Check if user found all mathcing sets then shows completed board and resets the game
##    15. Asks user if they want to play again
##
##Error Handling: 
##
##Other Comments: 
##
##################################################################################
import string
import random

class Cell(object):

    def __init__(self, value):
        """
        :param value: The value that is currently in the cell.
        Initializes the cell with the value and sets it to not visible.
        :return:
        """

        self.value = value
        
    
    def __eq__(self, compare):
        """
        :param compare: Returns True if both instances have the same value.  False if not
        :return:
        """

        self.compare = compare
        return False

    def __str__(self):
        """
        :return: Returns the String representation of the cell.
                * if it is not visible.
                The value if it is visible.
        """
        
        return self.user_board 

    def flip(self):
        """
        Flips over the cell.  Shows it, it if it was hidden.  Hides it, if it was shown.
        :return: None
        """

        self.flip =  self
        print(self.flip)


class Board(object):

    def __init__(self, size):
        """
        :param size: Sets up the instance given the size.
                size 1 : 3 x 4
                size 2 : 4 x 5
                size 3 : 4 x 6

        :return:
        Exceptions  : Raises a Value Error if the size is not 1, 2 or 3
                    raise ValueError("size must be 1, 2 or 3")
        """
        
        self.size = size


#Checks for valid input difficulty
        try:
            while self.size <= 0 or self.size >= 4:
                print("You can only enter 1, 2, or 3 as the difficulty")
                user_difficulty = int(input("How difficult should the game? (1,2,3):"))

                self.size = user_difficulty
        except ValueError:
            print("You must enter an integer from 1 to 3")

        #Base main board with rows increased depending on difficulty
        self.main = []
        game_board_row1 = ['A','B','C','D']
        game_board_row2 = ['E','F','F','E']
        game_board_row3 = ['D','C','B','A']
        
        game_board_row4 = ['G','H','H','G']
        game_board_row1_2 = ['A','B','C','D','I']
        game_board_row2_2 = ['E','F','F','E','I']
        game_board_row3_2 = ['D','C','B','A','J']
        game_board_row4_2 = ['G','H','H','G','J']

        game_board_row1_3 = ['A','B','C','D','I','K']
        game_board_row2_3 = ['E','F','F','E','I','K']
        game_board_row3_3 = ['D','C','B','A','J','L']
        game_board_row4_3 = ['G','H','H','G','J','L']
        
        if self.size == 1:
            self.main.append(game_board_row1)
            self.main.append(game_board_row2)
            self.main.append(game_board_row3)

            self.user_board = [['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*']]
            self.hidden_board = [['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*']]

        if self.size == 2:
            self. main.append(game_board_row1_2)
            self.main.append(game_board_row2_2)
            self.main.append(game_board_row3_2)
            self.main.append(game_board_row4_2)

            self.user_board = [['*', '*', '*', '*','*'], ['*', '*', '*', '*','*'], ['*', '*', '*', '*','*'], ['*', '*', '*', '*','*']]
            self.hidden_board = [['*', '*', '*', '*','*'], ['*', '*', '*', '*','*'], ['*', '*', '*', '*','*'], ['*', '*', '*', '*','*']]

        if self.size == 3:
            self.main.append(game_board_row1_3)
            self.main.append(game_board_row2_3)
            self.main.append(game_board_row3_3)
            self.main.append(game_board_row4_3)

            self.user_board = [['*', '*', '*', '*','*','*'], ['*', '*', '*', '*','*','*'], ['*', '*', '*', '*','*','*'], ['*', '*', '*', '*','*','*']]
            self.hidden_board = [['*', '*', '*', '*','*','*'], ['*', '*', '*', '*','*','*'], ['*', '*', '*', '*','*','*'], ['*', '*', '*', '*','*','*']]
            
        return 





    def __str__(self):
        """
        :return: String representation of the state of the board.
        """

        #This is what the user sees as his board
        if self.size == 1:
            print("     1    2    3    4")
            print("1|",self.user_board[0])
            print("2|",self.user_board[1])
            print("3|",self.user_board[2])


        if self.size == 2:
            print("     1    2    3    4    5")
            print("1|",self.user_board[0])
            print("2|",self.user_board[1])
            print("3|",self.user_board[2])
            print("4|",self.user_board[3])

        
        if self.size == 3:
            print("     1    2    3    4    5    6")
            print("1|",self.user_board[0])
            print("2|",self.user_board[1])
            print("3|",self.user_board[2])
            print("4|",self.user_board[3])

            
        return 





    def guess_input(self):
        """Asks user for first guess"""
        
        self.user_guess_y = int(input("What row?:"))

        self.user_guess_x = int(input("What column?:"))

    #Shows user of current board
        print(self.__str__())

        return
        
    
    def validate_choice(self, row, col):
        """
        :param row: the row being validated
        :param col: the column being validated
        :return: : None
        Exceptions.  Throws a ValueError if the row or column is not in the legals values
                    Also throws a ValueError if the cell is already being shown.
        """

        self.row1 = row
        self.col1 = col
        
    #Temporarily holds the users guess
        try:
            self.guess_holder = self.main[self.user_guess_y][self.user_guess_x]

    #Tells user that he exceeded the boards size
        except IndexError:
            print("Row or Column is not in the legals values")
            self.guess_input()
            self.validate_choice(self.user_guess_y, self.user_guess_x)
            
        return      


    def play_choice1(self, row, col):
        """
        If the row, column is valid then it uncovers that row and column.
        :param row: int
        :param col: int
        :return: None
        """

    #Moves user guess to first choice so original guess can be reset later
        self.first_guess_holder = self.guess_holder
        self.user_guess_y1 = self.user_guess_y
        self.user_guess_x1 = self.user_guess_x

        return
    
    def play_choice2(self, row, col):
        """
        If the row, column is valid then it uncovers that row and column.
        :param row: int
        :param col: int
        :return: None
        """

    #Moves user guess to second choice so original guess can be reset later
        self.second_guess_holder = self.guess_holder
        self.user_guess_y2 = self.user_guess_y
        self.user_guess_x2 = self.user_guess_x        
   
        return


    def end_turn(self):
        """ If the cells were not a match, then it flips the user choices back over.
        :return: None
        """
    #Moves the current user_board to a temporary board to check guesses
        self.flipped_board = self.user_board
        

    #Shows both flipped cards by replacing user guesses to the unhidden main board
        self.flipped_board[self.user_guess_y1][self.user_guess_x1] = self.main[self.user_guess_y1][self.user_guess_x1]
        self.flipped_board[self.user_guess_y2][self.user_guess_x2] = self.main[self.user_guess_y2][self.user_guess_x2]
     

    #Next step is to check if the 2 values are the same

        # if not then the board is reset back to the hidden board
        if self.first_guess_holder != self.second_guess_holder:

        #Unmatching guesses are set back to hidden
            self.flipped_board[self.user_guess_y1][self.user_guess_x1] = self.hidden_board[self.user_guess_y1][self.user_guess_x1]
            self.flipped_board[self.user_guess_y1][self.user_guess_x1] = self.hidden_board[self.user_guess_y1][self.user_guess_x1]

            self.flipped_board[self.user_guess_y2][self.user_guess_x2] = self.hidden_board[self.user_guess_y2][self.user_guess_x2]
            self.flipped_board[self.user_guess_y2][self.user_guess_x2] = self.hidden_board[self.user_guess_y2][self.user_guess_x2]

            self.user_board = self.flipped_board
            

    #If guesses are same, then now the hidden board, will premamntly show the two equal values
        if self.first_guess_holder == self.second_guess_holder:
            self.user_board = self.flipped_board
            
    #Resets the temporary flipped board back to hidden
        self.flipped_board = self.hidden_board
        print()

    #Checks if the user guessed all the matching values
        self.game_over()
        return 

    
    def game_over(self):
        """
        :return: bool - True if all the cells are uncovered, False if not.
        """

    #If the user guessed all matching values, then it will print complete board, resets all boards, and ask user if they want to play again
        if  self.user_board == self.main:
            print("Congrats all pairs found")
            print(self.main)

            #Resets boards

            self.user_board = self.hidden_board
            self.flipped_board = self.hidden_board



            self.again = input("Do you want to play again? Type, Y/YES/N/NO:")
            self.again.upper()


            if self.again == "Y" or self.again == "YES":
                print("Restarting Game")
                self.game_over is not False

            if self.again == "N" or self.again == "NO":
                print("Ending Game")
                self.game_over is not True

            

            else:
                self.game_over is not True

        else:
            return False



#This starts the board and keeps looping while the game is playing
if __name__ == "__main__":

    #Connects to cell class
    memory_game_temp = Cell(Board)

#Asks user of game difficult and catches any mal input
    try:
        user_difficulty = int(input("How difficult should the game be? (1,2,3):"))
        
    #Connects the game to the class Board
        memory_game = Board(user_difficulty)
        print()

    #Shows user the starting board
        print("Memory Board")
        memory_game.__str__()
        print()

#Step 2 Taking in User Guesses Input
    #First Guess
        while memory_game.game_over is not False:
            memory_game.guess_input()
            memory_game.validate_choice(memory_game.user_guess_y, memory_game.user_guess_x)
            memory_game.play_choice1(memory_game.user_guess_y, memory_game.user_guess_x)
            print()
            
    #Second Guess
            memory_game.guess_input()
            memory_game.validate_choice(memory_game.user_guess_y, memory_game.user_guess_x)
            memory_game.play_choice2(memory_game.user_guess_y, memory_game.user_guess_x)
        

#Flips values
            memory_game.end_turn()




    except ValueError:
        print("You must enter an integer from 1 to 3")
        user_difficulty = int(input("How difficult should the game? (1,2,3):"))

        memory_game = Board(user_difficulty)
        
    except TypeError:
        print("You must enter an integer from 1 to 3")
    except ZeroDivisionError:
        print()

        









    pass
