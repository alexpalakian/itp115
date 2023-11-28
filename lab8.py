# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Lab 8

import random
def coin():
    headsOrTails = random.randint(0, 1)
    if headsOrTails == 0:
        return "heads"
    else:
        return "tails"

def experiment():
    numHeadsInARow = 0
    numFlips = 0

    while numHeadsInARow != 3:
        result = coin()
        numFlips = numFlips + 1
        if result == "heads":
            numHeadsInARow = numHeadsInARow + 1
        else:
            numHeadsInARow = 0
    return numFlips

def main():
    totalNumberOfFlips = 0
    for x in range(10):
        result = experiment()
        totalNumberOfFlips = totalNumberOfFlips + result
    answer = (totalNumberOfFlips / 10)
    print("The average for 3 heads in a row is:", answer)

main()