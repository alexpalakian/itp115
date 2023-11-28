# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Lab 4

def main():

    symbolWithSpace = "# "
    outerSpace = " "
    numSymbol = -1
    numSpace = 20

    for symbol in symbolWithSpace:
        while numSymbol <= 18:
            numSpace = int(numSpace - 2)
            numSymbol = int(numSymbol + 2)
            print((outerSpace * numSpace) + (symbolWithSpace * numSymbol))

main()
