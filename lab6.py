# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Lab 6

def main():

    userWordOne = input("Enter word #1: ")
    userWordTwo = input("Enter word #2: ")

    wordOne = userWordOne.lower()
    wordTwo = userWordTwo.lower()

    aStringOne = wordOne.replace(" ", "")
    aStringTwo = wordTwo.replace(" ", "")

    aListOne = list(aStringOne)
    aListTwo = list(aStringTwo)

    aListOne.sort()
    aListTwo.sort()

    if len(aListOne) == len(aListTwo) and aListOne == aListTwo:
        print("The words are anagrams!")
    else:
        print("The words are NOT anagrams.")
    print()
    userPhrase = input("Enter a phrase: ")

    stringPhrase = userPhrase.replace(" ", "")

    aListPhrase = list(stringPhrase)
    aListPhrase.reverse()
    newPhrase = "".join(aListPhrase)


    if newPhrase.lower() == stringPhrase.lower():
        print("The phrase is a palindrome!")
    else:
        print("The phrase is NOT a palindrome.")

main()