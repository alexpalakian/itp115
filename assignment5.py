# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Assignment 5
# Description: in this program, the user can enter a sentence and program will reveal if the sentence contains any special
#              characters as well as show the character distribution

def main():

    print("Character Distribution")
    runAgain = int(input("Enter the number of times to run: "))
    # I will get a user to input an integer; need int(input() because of that; this is the number of times the program will run
    # and ask the user for a sentence
    for number in range(runAgain):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        print()
        # above is a space
        userSentence = input("Enter a sentence: ")
        #  I used a range based for loop to accomplish asking the user how many times they want to run the program
        # because the user will enter an integer.
        # a range based for loop is a loop that runs a specific number of times and on a sequence; in this case the
        # sequence is a range of integers.
        # essentially for every number in the runAgain user input number, this program will run; for example
        # if the user entered 2, it will run once, and then it will run twice.
        # the alphabet is a variable that contains all the letters in the alphabet
        # in userSentence, I am asking the user to enter a sentence

        stars = 0
        # stars variable will be counting the number of special characters and stores the value into stars; acts as a counter
        for letter in userSentence.lower():
            if letter not in alphabet and letter != " ":
                stars = stars + 1
                # the program will run for every letter in the user sentence, and check if each letter is not in the alphabet
                # (using my alphabet variable), and not a space (" ")
                # every time with is true for each letter in the sentence, my stars counter will increase by one
                # this is the amount of special characters there are in an integer form

        # this is after the for loop above

        if stars == 0:
            print("Special character: NONE")
            # stars will be equal to zero if there are no special characters, thus it will print NONE
        else:
            print("Special character: " + str("*" * stars))
            # by using branching, I can separate from when stars is zero or more than zero
            # here, if stars is any number, the program will run this code
            # I am multiplying the stars by using the multiplication operator (number of special characters) by * and
            # converting that in a string to document the special characters

        # next I will use a nested for loop
        # a nested for loop includes an outer for loop and an inner for loop (two for loops)

        for character in alphabet:
        # conceptually: for every character (letter) in the alphebet; the program will run through each character in the alf
            counter = 0
            # this variable is counting the character (every letter in the alphabet) and stores the value into counter
            for special in userSentence.lower():
            # conceptually: for every special (letter) in the inputted sentence; the program will run through
            # each special (letter) in sentence and analyze it
                if character == special:
                    counter = counter + 1
                    # conceptually: if the character in the alphabet is in the special of the sentence...
                    # then everytime this is true per character in the alphabet, the counter will increase by one
            if counter == 0:
                print(character + ": NONE")
                # if the counter is zero, meaning the letter in the alphabet does not appear in the user sentence,
                # the program will print NONE next to the alphabet letter the sentence does not contain
            else:
                print(character + ":", str("*" * counter))
                # however, if the counter is more than zero (a letter in the alphabet DOES appear in the user sentence)
                # the program will print a certain amount of * the counter contains
                # this is done by using the multiplication operator and converting that to a string to be printed in * form

main()