# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Assignment 1
# Description: This program will display two truths and a lie about myself!

def main():
    # def main() is the start of my code, and main() is the end
    # all code should be between those and tabbed over once
    first = "Alex"
    last = "Palakian"
    # character string (str): anything with quotation marks around it
    # I am assigning such strings into variables to create two str variables
    print("Full name:", first, last)
    # the use of a , is to concatenate the string and str variables together when outputted by adding a space between
    # The string within quotations and my two string variables will be outputted together
    print()
    # the () above is to output an empty line for separation
    pets = 2
    siblings = 1
    # integer (int): any number without a decimal
    # I am assigning the integer 2 and 1 into variables pets and siblings respectively, creating two int variables
    print("Number of pets:", pets)
    print("Number of siblings:", siblings)
    # My output will be the string within quotes and my int variables I assigned, respectively
    print()
    # the code above is to output an empty line for separation
    statement1 = "I have a twin sister."
    statement2 = "I have broken my wrist four times."
    statement3 = "My favorite fruit is raspberries."
    # I am assigning strings (my truths and lie) into variables to create three str variables
    print("Statement 1:", statement1)
    print("Statement 2:", statement2)
    print("Statement 3:", statement3)
    # The string within quotes and my str variables will be outputted, respectively
    print()
    # the code above is to output an empty line for separation
    truth1 = True
    truth2 = True
    truth3 = False
    # boolean (bool): True or False; the first letter needs to be capitalized
    # I am assigning a true or false answer into such variables to create three bool variables
    print("Statement 1 is", truth1)
    print("Statement 2 is", truth2)
    print("Statement 3 is", truth3)
    # the string within quotes and my bool variables will be outputted, respectively
    # when ran, this code will display my two truths and a lie! Can you guess the lie?
main()