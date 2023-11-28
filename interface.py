# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Final Project
# interface.py
# Description: this file creates 8 functions while using the functions from tasks.py file. This file uses the foundational
# functions in tasks.py as inputs to create functions for each menu option. This file is the meat of the program, coding for
# each option regardless of user input. These major functions will later be pieced together

# this imports the functions from tasks.py file
import tasks

# parameters: none
# return: a dictionary where are keys are the letters and the menu options are the values
# this function manually creates a dictionary to display each option for each letter
def getMenuDict():
    letterDict = {"A":"All national parks", "B":"Parks in a particular state", "C":"The largest park", "D":"Search for a park", "Q":"Quit"}
    return letterDict

# parameters: menu dictionary (from getMenuDict())
# return: none
# this function displays the menu as a side effect is a specific format
def displayMenu(menuDict):
    key = list(menuDict.keys())
    # the .keys() command creates a list of keys from a dictionary
    print(key[0], "->", menuDict["A"])
    print(key[1], "->", menuDict["B"])
    print(key[2], "->", menuDict["C"])
    print(key[3], "->", menuDict["D"])
    print(key[4], "->", menuDict["Q"])
    # I indexed each key and printed each one with their respective values

# parameters: menu dictionary (from getMenuDict())
# return: the choice entered by the user
# this function gets input from the user and makes sure the input is appropriate
def getUserChoice(menuDict):
    userChoice = input("Choice: ")
    key = list(menuDict.keys())
    # the .keys() command creates a list of keys from a dictionary
    while userChoice.upper() not in key:
        userChoice = input("Choice: ")
        # if the user choice is not in the list of keys, then the function will ask for another choice
    return userChoice.upper()
    # returns the choice is upper case

# parameters: list of parks where each park is a dictionary (from readParksFile())
# return: none
# this function loops through each park dict and prints information out in a specific format
def printAllParks(parksList):
    index = 0
    # a counter
    while index <= 55:
        # I chose 55 because there are 56 dicts of parks
        dictionary = parksList[index]
        # each time, it will take out a new park dict from the list and analyze it
        name = dictionary["Name"]
        code = dictionary["Code"]
        location = dictionary["State"]
        area = dictionary["Acres"]
        date = dictionary["Date"]
        # stores the value of each dict in variables
        newDate = tasks.convertDate(date)
        # inputs the numerical date into the convertDate() function from tasks.py file
        print(name, "(" + code + ")")
        print("\tLocation:", location)
        print("\tArea:", area, "acres")
        print("\tDate Established:", newDate)
        # prints each park (as a side effect) in a certain format; used \t command to tab over information
        index = index + 1
        # each time the loop runs, one is added to mark off each park

# parameters: none
# return: a strong with a state abbreviation (must be two letters)
# this function gets the user to enter a state and if it is not two letters, will ask again
def getStateAbbr():
    userState = input("Enter a state: ")
    while len(userState) != 2:
        # the len() command gets the length of the user input; if it is not two letters the loop will run
        print("Need the two letter abbreviation")
        userState = input("Enter a state: ")
    return userState.upper()
    # returns the user state in upper case regardless if it is an actual state or not (only needs to be two letters)

# parameter: list of parks where each park is a dictionary (from readParksFile())
# return: none
# this function prints all the parks within the state the user entered in getStateAbbr() function
def printParksInState(parksList):
    state = getStateAbbr()
    # stores the getStateAbbr() return into a variable
    index = 0
    numberOfParks = 0
    # counters
    while index <= 55:
        # I chose 55 because there are 56 dicts of parks
        dictionary = parksList[index]
        # each time, it will take out a new park dict from the list and analyze it
        location = dictionary["State"]
        if state in location:
            # if the state the user entered the "State" value from each park dict are the same...
            name = dictionary["Name"]
            code = dictionary["Code"]
            area = dictionary["Acres"]
            date = dictionary["Date"]
            newDate = tasks.convertDate(date)
            print(name, "(" + code + ")")
            print("\tLocation:", location)
            print("\tArea:", area, "acres")
            print("\tDate Established:", newDate)
            # the values from the park dicts are acquired and printed as a side effect is a specific format
            numberOfParks = numberOfParks + 1
            # if the "State" value and user state are the same, then one will be added
        index = index + 1
        # each time the loop runs, one is added to mark off each park

    if numberOfParks == 0:
        print("There are no national parks in", state, "or it is not a valid state.")
        # if the "State" value and user state are not the same for any park dict, this statement will be printed

# parameter: list of parks where each park is a dictionary (from readParksFile())
# return: none
# this function uses the getLargestPark() function and prints out information from the largest park
def printLargestPark(parksList):
    largestPark = tasks.getLargestPark(parksList)
    # stores the getLargestPark() return value
    index = 0
    while index <= 55:
        # I chose 55 because there are 56 dicts of parks
        dictionary = parksList[index]
        # each time, it will take out a new park dict from the list and analyze it
        code = dictionary["Code"]
        if code == largestPark:
            # if the "Code" value and getLargestPark() return are the same...
            name = dictionary["Name"]
            location = dictionary["State"]
            area = dictionary["Acres"]
            date = dictionary["Date"]
            newDate = tasks.convertDate(date)
            description = dictionary["Description"]
            print(name, "(" + code + ")")
            print("\tLocation:", location)
            print("\tArea:", area, "acres")
            print("\tDate Established:", newDate)
            print("\tDescription:", description)
            # the values from the park dicts are acquired and printed as a side effect is a specific format
        index = index + 1
        # each time the loop runs, one is added to mark off each park

# parameters: list of parks where each park is a dictionary (from readParksFile())
# return: none
# this function asks the user to enter a search term and loops through each park dict to see if the user word is in
# the "Code" "Name" or "Description" value of each park dict
def printParksForSearch(parksList):
    userSearch = input("Enter text for searching: ")
    newUserSearch = userSearch.lower()
    # asks the under to enter a search word and makes it lowercase
    index = 0
    numberOfParks = 0
    # counters
    while index <= 55:
        # I chose 55 because there are 56 dicts of parks
        dictionary = parksList[index]
        # each time, it will take out a new park dict from the list and analyze it
        name = dictionary["Name"]
        newName = name.lower()
        # each name value is translate to all lowercase
        location = dictionary["State"]
        code = dictionary["Code"]
        newCode = code.lower()
        # each code value is translate to all lowercase
        area = dictionary["Acres"]
        date = dictionary["Date"]
        newDate = tasks.convertDate(date)
        description = dictionary["Description"]
        newDescription = description.lower()
        # each description value is translate to all lowercase
        if newUserSearch in newCode or newUserSearch in newName or newUserSearch in newDescription:
            # of the user word is in the "Code" "Name" or "Description" values for each park dict...
            print(name, "(" + code + ")")
            print("\tLocation:", location)
            print("\tArea:", area, "acres")
            print("\tDate Established:", newDate)
            print("\tDescription:", description)
            numberOfParks = numberOfParks + 1
            # the values from the park dicts are acquired and printed as a side effect is a specific format
            # for each park that is in this branching, one is added
        index = index + 1
        # each time the loop runs, one is added to mark off each park

    if numberOfParks == 0:
        print("There are no national parks for the search text of \'" + newUserSearch + "\'.")
        # if the the user search word is not in any park dict, this statement will be printed