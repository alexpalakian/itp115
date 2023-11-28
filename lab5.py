# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Lab 5

import random
def main():

    nouns = ['france', 'pencil', 'carrot', 'pasta', 'shower']
    verbs = ['swam', 'skied', 'texted', 'frolicked']
    adverbs = ['cheerfully', 'savagely', 'carefully', 'enormously']

    userInput = 0
    while userInput != 5:
        print("Welcome to the Sentence Generator")
        print("1. View words")
        print("2. Add Noun")
        print("3. Remove Verb")
        print("4. Generate sentence")
        print("5. Exit")
        userInput = int(input(("> ")))

        if userInput == 1:
            print("nouns:", nouns)
            print("verbs:", verbs)
            print("adverbs:", adverbs)
        elif userInput == 2:
            newNoun = input("Enter a word (noun): ")
            if newNoun not in nouns:
                nouns.append(newNoun)
            else:
                print("Sorry that noun is already in the list of nouns!")
        elif userInput == 3:
            verbRemove = input("Enter the word (verb): ")
            if verbRemove in verbs:
                verbs.remove(verbRemove)
            else:
                print("Sorry that is not in the list of verbs!")
        elif userInput == 4:
            firstWord = random.choice(nouns)
            secondWord = random.choice(verbs)
            thirdWord = random.choice(adverbs)
            print(firstWord, secondWord, thirdWord)
        elif userInput != 1 and userInput != 2 and userInput != 3 and userInput != 4 and userInput != 5:
            print("Invalid choice")
        else:
          print("Thank you for using the Sentence Generator!")

main()