# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Assignment 2
# Description: This program creates a Mad Libs story by getting input from the user to print an output
def main():
    number1 = int(input("Enter a number (greater than 1): "))
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a toy (singular): ")
    number2 = int(input("Enter a second number (greater than 1): "))
    food = input("Enter a food (plural): ")
    adjective2 = input("Enter a color: ")
    emotion = input("Enter an emotion (adjective): ")
    decimal = float(input("Enter a number with a decimal: "))
    number3 = int(input("Enter a third number: "))
    # all of these variables have input, meaning we can ask the user to type in information (assign) which can be stored
    # using the input function
    # the variables to which the message is a string will only need input()
    # the variables to which the number is an integer of a float will need int() or float() before the input()
    # this is because input always returns a strings.
    # I left a space after : to make it more aesthetic for the user
    # overall these variables will have a user value stored and later outputted when implemented
    print()
    # this code allows for an empty line to be outputted (for separation)
    print("Today I went to the beach with my \"" + str(number1) + "\" friends and we brought a \"" + adjective1 + "\"")
    # In order to output the variables in quotations, I use the escape character \"
    # because the number1 variable is an integer, I need to convert it to a string and add str() before the variable
    # by concatenating the variables with the escape character using +, no spaces will be outputted--making it seamless
    print("\"" + noun1 + "\" because we wanted play. Also, we packed \"" + str(number2 * number1) + "\" \"" + food + "\" to eat")
    # I used the arithmetic operation of multiplication to multiply two integers together and converted the product to a string to be outputted
    print("later. However, when we were swimming in the \"" + adjective2 + "\" ocean, a seagull swooped down and ate our food!")
    print("It made us really \"" + emotion + "\". So, because we had no food and it was \"" + str(decimal) + "\"")
    # I have to convert the decimal (float) into a string inorder for it to be outputted
    print("degrees fahrenheit, we left the beach to get an ice cream. The creamery was only \"" + str(number3 + number2) + "\"")
    # I used the arithmetic operation of addition to add two integers together; this will sum the user input together to create an integer
    print("minutes away.")
    # I used multiple print() statements to print out the story with the user's words injected
    # overall, by printing strings concatenating input variables within the story, I am able to make a mad lib that corresponds with user input
main()
