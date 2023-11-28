# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Final Project
# main_palakian_alex.py
# Description: this file uses all functions from the two previous files and pieces everything together in one function
# in an organized way via branching. It calls such functions based on the user choice and implements the functions appropriately

# this imports the functions from tasks.py file and interface.py file
import tasks
import interface

# parameters: none
# return: none
# this function essentially runs the program. It calls functions from both files and uses branching to organize
# which function to run based on the user choice all within a while loop
def main():
    print("National Parks")
    print()
    # space
    parksList = tasks.readParksFile()
    # stores the list of park dicts in this variable
    menu = interface.getMenuDict()
    # stores the menu dict in this variable
    interface.displayMenu(menu)
    # displays menu options
    userChoice = interface.getUserChoice(menu)
    # stores user choice into this variable
    while userChoice != "Q":
        if userChoice == "A":
            interface.printAllParks(parksList)
            # calls the printAllParks() function
            print()
            # space
            interface.displayMenu(menu)
            # displays menu options
            userChoice = interface.getUserChoice(menu)
            # asks the user to choose again based on the menu display
        elif userChoice == "B":
            interface.printParksInState(parksList)
            # calls the printParksInState() function
            print()
            # space
            interface.displayMenu(menu)
            # displays menu options
            userChoice = interface.getUserChoice(menu)
            # asks the user to choose again based on the menu display
        elif userChoice == "C":
            interface.printLargestPark(parksList)
            # calls the printLargestPark() function
            print()
            # space
            interface.displayMenu(menu)
            # displays menu options
            userChoice = interface.getUserChoice(menu)
            # asks the user to choose again based on the menu display
        elif userChoice == "D":
            interface.printParksForSearch(parksList)
            # calls the printParksForSearch() function
            print()
            # space
            interface.displayMenu(menu)
            # displays menu options
            userChoice = interface.getUserChoice(menu)
            # asks the user to choose again based on the menu display

            # through branching, the appropriate function is called
main()