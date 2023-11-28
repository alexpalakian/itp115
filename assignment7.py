# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Assignment 7
# Description: this programs allows the user to play rock-paper-scissors against the computer using assigned integers.
#              the programs will also have the option to repeat, display the winner, and count the results--utilizing a
#              series of functions.

import random
# this code allows the programs to use the random function

def displayRules():
    print("Let's play Rock Paper Scissors.")
    print("The rules of the game are:")
    print("\tRock smashes Scissors")
    print("\tScissors cut Paper")
    print("\tPaper covers Rock")
    print("\tIf both the choices are the same, it's a tie")
    # parameters (input): none
    # return: none
    # this function prints of rules of the game using print statements
    # the print statements are side effects that will be shown when called
    # the \t special character tabs the message over

def getComputerNum():
    return random.randint(0, 2)
    # parameters (input): none; meaning there is no parameter that goes into the function
    # return: a random integer between 0-2 inclusive
    # this function used the random.randint command to pick a random int within the set range

def getPlayerNum():
    print("Enter 0 for Rock, 1 for Paper, or 2 for Scissors")
    playerNum = int(input("> "))
    while playerNum != 0 and playerNum != 1 and playerNum !=2:
        playerNum = int(input("> "))
    return playerNum
    # parameters (input): none
    # return: an integer that represents the user's choice based on the input statement
    # this function has a side effect of a print statement when used
    # this function needs the int to be between 0-2, thus error checking via a while loop is employed
    # once the int is between 0-2, the playerNum is returned

def playRound(computerNum, playerNum):
    if computerNum == 0 and playerNum == 0:
        return 0
    elif computerNum == 0 and playerNum == 1:
        return 1
    elif computerNum == 0 and playerNum == 2:
        return -1
    elif computerNum == 1 and playerNum == 0:
        return -1
    elif computerNum == 1 and playerNum == 1:
        return 0
    elif computerNum == 1 and playerNum == 2:
        return 1
    elif computerNum == 2 and playerNum == 0:
        return 1
    elif computerNum == 2 and playerNum == 1:
        return -1
    elif computerNum == 2 and playerNum == 2:
        return 0
    # parameters (input): an int representing the computer choice AND an int representing the player choice
    # return: an int the represents a tie or winner
    # this function is essentially the game to which the program runs through every possible outcome
    # through branching, the program returns values that are representative of a player win (1), computer win (-1) , or tie (0)
    # the results are determined by the inputs which come from getComputerNum() and getPlayerNum functions
    # 0 is rock, 1 is paper, and 2 is scissors; the return values are based on game logic

def continueGame():
    yOrN = input("Do you want to continue playing (y or n)? ")
    if yOrN == "y" or yOrN == "Y":
        return True
    else:
        return False
    # parameters (input): none
    # return: boolean
    # this function determines if the user want to play another game
    # after an input statement, y (lower of cap) returns the boolean True, and anything else returns the boolean False

def main():
# def main() function has no parameters or return value
    tieCounter = 0
    playerWinCounter = 0
    computerWinCounter = 0
    # these variables are counters that will be changed depending on the results of the game
    # because no game has been played, all values are set to 0

    userContinue = True
    while userContinue == True:
    # this is a do-while loop that will automatically run through one game before having the option to change
    # I used a boolean to determine the userContinue loop

        displayRules()
        # I am calling the displayRules() function
        computerNumber = getComputerNum()
        # I am calling the getComputerNum() function and store its return value into a variable
        userNumber = getPlayerNum()
        # I am calling the getComputerNum() function and store its return value into a variable
        gameResult = playRound(computerNumber, userNumber)
        # I am calling the playRound() function and inputting the variables that store the return values
        # based on the playRound() function return values, the gameResult variable will either store -1, 0, or 1
        if gameResult == -1:
            print("Computer wins.")
            computerWinCounter = computerWinCounter + 1
        elif gameResult == 0:
            print("You and the computer tied.")
            tieCounter = tieCounter + 1
        elif gameResult == 1:
            print("You win!")
            playerWinCounter = playerWinCounter + 1
        # using branching, print statements will be outputted based on the variable; -1: computer wins; 0: tie, 1: player wins
        # whichever result occurs, the respective variable counter will increase by 1 everytime the outcome happens
        userContinue = continueGame()
        # I am calling the userContinue() function and store its return value into a variable
        # if the return is True the loop will repeat; anything else (False) the loop will stop
        print()
        # codes a space

    print("You won", str(playerWinCounter), "game(s).")
    print("The computer won", str(computerWinCounter), "game(s).")
    print("You tied with the computer", str(tieCounter), "time(s).")
    # once the loop ends, these print statements will be outputted
    # by concatenating variable counters with strings, these statements print the numerical results of all games played

main()