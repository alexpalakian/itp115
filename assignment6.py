# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Assignment 6
# Description: this program will display a jumbled word to the user the and user will have to guess the scrambled word.
#              Hints will also be offered and the number of guesses it takes will be documented

import random
# this will allow my program to use the random function
def main():

    words = ["ocean", "february", "cactus", "guitar"]
    hints = ["beach", "month", "succulent", "instrument"]
    # these are lists that include a sequence of stings
    # a list is mutable, meaning they can be modified with code.

    theWord = random.choice(words)
    index = words.index(theWord)
    theHint = hints[index]
    # using the random.choice() I am storing a random string from the words list into a variable
    # by using .index on the random word I am storing the index (the position of the word in the list) into a variable
    # I am using the index of the random word to get its corresponding hint by employing [index] to the hint list

    jumbledWord = list(theWord)
    # by using the list() function, I am converting the string into a list of letters; now each letter is mutable
    jumble = ""
    # this is my empty string to store the soon-to-be-created jumbled word

    i = 0
    # i is my counter; in this case it involves the length of the word
    while i < len(theWord):
        letter = random.choice(jumbledWord)
        jumble = jumble + letter
        jumbledWord.remove(letter)
        i = i + 1
        # I am using a while loop to loop through the jumbledWord (the one with the lists of letters) and randomly selecting
        # a letter each time by using the random.choice() function
        # I am then adding the random letter to the empty string using the addition operator
        # in order to remove the selected word from the list in order not to be selected twice, I .remove() the word from the list
        # I then add 1 to the counter because the empty string now included a letter
        # the while loop will stop once jumble is the same length as theWord. I did this by comparing i to the length of theWord
    print("The jumbled word is \"" + jumble + "\"")
    # I used special characters to print out jumble in quotation marks

    userGuess = input("Enter your guess: ")
    counter = 1
    # my counter is one because the user starts out with 1nguess before offering hints
    while userGuess != theWord:
        print("That is not correct")
        counter = counter + 1
        yesOrNo = input("Do you want a hint (y or n)? ")
        # if the userGuess is not theWord, then my program will string a message and ask the user (using input), if they
        # want a hint
        # because this loop will run every time the user guesses a word, I increase the counter by 1 everytime to tack the
        # number of guesses the user takes
        if yesOrNo.lower() != "y":
            print("The jumbled word is \"" + jumble + "\"")
            userGuess = input("Enter your guess: ")
            # if the user selects any letter other than y when asked if they want a hint, this code will run:
            # the jumbled word will be repeated the  user will be asked again to enter a word
        else:
            print("Your hint is:", theHint)
            print("The jumbled word is \"" + jumble + "\"")
            userGuess = input("Enter your guess: ")
            # if the user selected y when asked for a hint, this code will run:
            # a previously stored hint will be printed, the jumbled word will be printed, and the user will be asked again
            # to enter a word

    print("You got it!")
    print("It took you", counter, "guesses.")
    # the loop will end once the userGuess matched theWord, and the code will run these messages
    # I also printed the counter to include how many guesses it took the user to win the game

main()