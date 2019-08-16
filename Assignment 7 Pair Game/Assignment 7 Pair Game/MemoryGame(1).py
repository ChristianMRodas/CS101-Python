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
        print(self.value)
        pass
    
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
        
        return user_board #I think

    def flip(self):
        """
        Flips over the cell.  Shows it, it if it was hidden.  Hides it, if it was shown.
        :return: None
        """

        self.flip =  self
        print(self.flip)
        print()
        pass

#None of the below functins should have more than 15 lines of code
#Should have a try and except
# You may have to "raise" an error
#   so like raise ValueError
# or like in a function then it looks like
#   def f1(h):
#       if n < 0:
        #raise ValueError


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
        
        self.board = self #?
        self.size = size

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
            
        print(self.main)
        return None





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

            
        return #So this is what the user has guessed correclty so far---- end==





    def guess_input(self):
        """Asks user for first guess"""
        
        self.user_guess_y = int(input("What row?:"))

        self.user_guess_x = int(input("What column?:"))

        return None
        
    
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

        try:

            #print(self.main[self.user_guess_y][self.user_guess_x])

            self.guess_holder = self.main[self.user_guess_y][self.user_guess_x]
            print("This is the value for the guess", self.guess_holder)
            print(self.__str__())

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

        self.first_guess_holder = self.guess_holder
        self.user_guess_y1 = self.user_guess_y
        self.user_guess_x1 = self.user_guess_x
        print("guess 1",self.user_guess_y1, self.user_guess_x1)
        print("holder value", self.first_guess_holder)

        #Next flip the value which is in another class


        
        None
    
    def play_choice2(self, row, col):
        """
        If the row, column is valid then it uncovers that row and column.
        :param row: int
        :param col: int
        :return: None
        """


        self.second_guess_holder = self.guess_holder
        self.user_guess_y2 = self.user_guess_y
        self.user_guess_x2 = self.user_guess_x        
        print("guess 2", self.user_guess_y2, self.user_guess_x2)
        print("holder value", self.second_guess_holder)

        
        return




    
    def end_turn(self):
        """ If the cells were not a match, then it flips the user choices back over.
        :return: None
        """

        print("user_board", self.__str__())
        self.flipped_board = self.user_board
        print("flipped board",self.flipped_board)

        #Shows both flipped cards

        self.flipped_board[self.user_guess_y1][self.user_guess_x1] = self.main[self.user_guess_y1][self.user_guess_x1]


        self.flipped_board[self.user_guess_y2][self.user_guess_x2] = self.main[self.user_guess_y2][self.user_guess_x2]
        print("second guess flipped", self.__str__())       

    #Next step is check if the 2 cards/ values are the same


        # if not then the board is reset back to the hidden board
        if self.first_guess_holder != self.second_guess_holder:
            print("Values are NOT the same, so values hide")


            self.flipped_board[self.user_guess_y1][self.user_guess_x1] = self.hidden_board[self.user_guess_y1][self.user_guess_x1]
            self.flipped_board[self.user_guess_y1][self.user_guess_x1] = self.hidden_board[self.user_guess_y1][self.user_guess_x1]

            self.flipped_board[self.user_guess_y2][self.user_guess_x2] = self.hidden_board[self.user_guess_y2][self.user_guess_x2]
            self.flipped_board[self.user_guess_y2][self.user_guess_x2] = self.hidden_board[self.user_guess_y2][self.user_guess_x2]

            self.user_board = self.flipped_board
            

    #Now the hidden board, will premamntly show the two equal values
        if self.first_guess_holder == self.second_guess_holder:
            print("Both values are the same")

            self.user_board = self.flipped_board
            


        self.flipped_board = self.hidden_board
        print()
        print("user",self.user_board)
        print("hidden", self.hidden_board)
        print("main",self.main)
        print("flipped",self.flipped_board)

        self.game_over()
        return self.user_board

    
    def game_over(self):
        """
        :return: bool - True if all the cells are uncovered, False if not.
        """


        
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
            print("not the same yet")
            return False



#this creates a board and keeps looping while the game is playing then end its finished
if __name__ == "__main__":

    #Connects to cell class
    #memory_game_temp = Cell()

    try:
        user_difficulty = int(input("How difficult should the game be? (1,2,3):"))

        memory_game = Board(user_difficulty)
        
        print()
        memory_game.__str__()


#Step 2 Taking in User Guesses Input
        print()

       
        
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
        
#Checks to make sure that the holds are holding
            print(memory_game.first_guess_holder, memory_game.second_guess_holder)

            print()


#Flips values
            memory_game.end_turn()




    except ValueError:
        print("You must enter an integer from 1 to 3")
        user_difficulty = int(input("How difficult should the game? (1,2,3):"))

        memory_game = Board(user_difficulty)
        
    #except TypeError:
        #print("You must enter an integer from 1 to 3")
    except ZeroDivisionError:
        print()

        









    pass
