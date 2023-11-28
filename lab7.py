# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Lab 7

def printRectangle(length, width):
    print(" " + str(width * "-") + " ")
    for rectangle in range(length):
        print("|" + str(width * " ") + "|")
    print(" " + str(width * "-") + " ")

def printSquare(size):
    print(" " + str(size * "-") + " ")
    for square in range(size):
        print("|" + str(size * " ") + "|")
    print(" " + str(size * "-") + " ")

def main():
    print("What shape would you like to print? ")
    print("r) rectangle")
    print("s) square")
    userShape = input("> ")

    if userShape.lower() == "r":
        userLength = int(input("Enter the length: "))
        userWidth = int(input("Enter the width: "))
        printRectangle(userLength, userWidth)

    elif userShape.lower() == "s":
        userSize = int(input("Enter the size: "))
        printSquare(userSize)

    else:
        print("That shape is not supported")

main()