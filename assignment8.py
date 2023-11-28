# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Assignment 8
# Description: create a program that uses call functions to code a game of Tic Tac Toe. In this program, two players will
#              alternate taking turns until there is a winner. The programs will also have the option to run again.

import TicTacToeHelper
def isValidNumber(boardList, position):
    if position >= 0 and position <= 8 and boardList[position] != "x" and boardList[position] != "o":
        return True
    else:
        return False
    # parameters: a list of representing the board AND an integer that corresponds to the index position the user would
    #             like to place their move on
    # return: boolean value
    # this function determines if the user position is between 0-8 and if the board includes x's or o's
    # using branching, the function will return True if the position between 0-8 and not taken up by x's or o's
    # the function will return False if the position is greater than 8 or taken up by by x's or o's

def updateBoard(boardList, position, playerLetter):
    boardList[position] = playerLetter
    # parameters: list representing the board AND an integer that corresponds to the index position the user would
    #             like to place their move on AND string representing user's letter ("x" or "o")
    # return: none
    # the function uses the position to index the board and replaces such position with the player's letter ("x" or "o")

def playGame():
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    # this list will become the boardList
    moveCounter = 0
    # this will track the moves everytime the while loop repeats
    winner = "n"
    # this variable matches the return value of checkForWinner() function and allows the loop to run [no winner yet]
    while winner == "n":
        alternate = moveCounter % 2
        # this variable allows player X and O to alternate turns where x is equal to 0 and O is any number--using
        # the modulus (1%2= number; 2%2= 0, 3%2= number, 4%2=0...)
        TicTacToeHelper.printUglyBoard(numbers)
        # I am calling the printUglyBoard() function and inputting the boardlist
        if alternate == 0:
            playerX = int(input("Player x, enter a number: "))
            # by using branching, I am able to alternatively ask each user to play but entering a num; player "x" starts
            valid = isValidNumber(numbers, playerX)
            while valid == False:
                playerX = int(input("Player x, enter a number: "))
                valid = isValidNumber(numbers, playerX)
                # I am storing the return of isValidNumber() function into a variable that can only work if the return
                # is True; if not, error checking will occur and ask the user for another number
            playerLetter = "x"
            updateBoard(numbers, playerX, playerLetter)
            # I am calling the updateBoard() function to input the boardlist, the user position number, and their symbol
            # "x" to perform the game of tic tac toe
            moveCounter = moveCounter + 1
            # everytime this series runs, it is a move (increases by one everytime)

        else:
            playerO = int(input("Player o, enter a number: "))
            # after player x goes, player o will be asked the same thing
            # this alternation is happening because of the modulus
            valid = isValidNumber(numbers, playerO)
            while valid == False:
                playerO = int(input("Player o, enter a number: "))
                valid = isValidNumber(numbers, playerO)
                # I am storing the return of isValidNumber() function into a variable that can only work if the return
                # is True; if not, error checking will occur and ask the user for another number
            playerLetter = "o"
            updateBoard(numbers, playerO, playerLetter)
            # I am calling the updateBoard() function to input the boardlist, the user position number, and their symbol
            # "o" to perform the game of tic tac toe
            moveCounter = moveCounter + 1
            # everytime this series runs, it is a move (increases by one everytime)
        winner = TicTacToeHelper.checkForWinner(numbers, moveCounter)

        # everytime the while loop runs the variable will match the return value of checkForWinner() function
        # once it is not "n" the game will stop
    TicTacToeHelper.printUglyBoard(numbers)
    # calling this function will visualize the three-in-a-row board
    print("Game over!")
    if winner == "s":
        print("Stalemate reached.")
    elif winner == "x":
        print("Player x is the winner!")
    elif winner == "o":
        print("Player o is the winner!")
        # this is what will be printed after the while loop ends
        # based on the key in checkForWinner() function: "s" is a stalemate; "x" is an X win; "o" is an O win
    # parameters: none
    # return: none
    # this overall purpose of this function is to program the game of tic tac toe by alternating user input through each
    # player and marking x's and o's on the board to determine the winner

def main():
    print("Let's play Tic Tac Toe!")
    playGame()
    keepPlaying = input("Would you like to play another round (y or n)? ")
    while keepPlaying.lower() == "y":
        playGame()
        keepPlaying = input("Would you like to play another round (y or n)? ")
    print("Goodbye!")
    # parameters: none
    # return: none
    # the purpose of main() function is to call the playGame() function while creating a while loop that
    # asks the user if they want to keep playing.

main()