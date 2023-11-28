# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Assignment 3
# Description:This program creates a Harry Potter vending machine that determines the change and gives a discount

def main():
    print("Please select an item from the vending machine:")
    print("\ta) Assortment of Candy for 11 sickles and 7 knuts")
    print("\tb) Butterbeer for 2 sickles")
    print("\tc) Quill for 6 sickles")
    print("\td) Daily Prophet for 5 knuts")
    # Here, I am outputting the four options to be displayed
    # I am using the escape character \t to tab over the options with outputted to be more visually pleasing
    choice = input("Choice: ")
    # I am using input in order to allow the user to decide which choice they want (user input)
    if choice.lower() == "a":
        item = "Assortment of Candy"
        cost = 326
    # by using an if statement, I am able to set up multiple conditions
    # by implementing .lower(), it automatically changes the users input to lower case--meaning the code will work for both upper and lower case
    # in this case, if they choose "a" then their chosen item and cost will be stored for later calculation
    # this same methodology and conceptualization applies to all other conditions below
    elif choice.lower() == "b":
        item = "Butterbeer"
        cost = 58
    elif choice.lower() == "c":
        item = "Quill"
        cost = 174
    elif choice.lower() == "d":
        item = "Daily Prophet"
        cost = 5
    # for all of the cost variables, I pre-calculated using the knut conversions provided in the instructions
    else:
        print("You entered an invalid choice, thus the item selected is the Butterbeer")
        item = "Butterbeer"
        cost = 58
    # this else statement means that if everything else is not true (the user's input doesn't match any other if/elif statement,
    # then this is the default option
    # in this case, I am assigning the choice of Butterbeer and its subsequent cost to the user because they entered an invalid choice
    print()
    # this code allows for an empty space for separation when outputted
    print("Please pay by entering the number of each coin")
    galleons = int(input("Number of galleons: "))
    sickles = int(input("Number of sickles: "))
    knuts = int(input("Number of knuts: "))
    # by using input I am allowing the user to type enter their various amounts and storing that into a variable
    # because user input is always a string I added int() to allow for an integer input
    print()
    # this code allows for an empty space for separation when outputted
    payment = int((galleons * 493) + (sickles * 29) + knuts)
    # this code is to calculate and convert the currency into knuts
    # using PEMDAS I multiplied the stored galleons (from the variable) by 493 because there are 493 knuts in 1 galleon
    # I multiplied the stored sickles (from the variable) by 29 because there are 29 knuts in 1 sickle
    # I added int() because the stored value would be an integer
    print("Cost in knuts:", cost)
    # what will be outputted is the cost value (that was stored in a variable) that corresponds to the user's choice
    print("Payment in knuts:", payment)
    # what will be outputted in the value of the payment (from the variable)
    print()
    # this code allows for an empty space for separation when outputted
    if payment < cost:
    # I am setting up a condition; if the payment is less than the cost then the user cannot afford their choice
        print("You did not enter enough money and will not receive the", item)
    # If this happens, python will instantly output the string with the user's choice item above and the code is done
    elif payment >= cost:
    # this is the second condition: if the payment is more than or equal to the cost then the user can afford their choice
        print("You purchased the", item)
        change = payment - cost
    # in order to get the amount of change I am subtracted the cost from the payment and stored that value is a variable
        print("Your change is", change, "knuts")
    # this string will output the respective amount of change the user will receive
        print("You will be given")
        galleonChange = change // 493
    # by using the division, I will get an integer (not a float)
    # I am dividing by 493 because there are 493 knuts in 1 galleon
        print("\tGalleons:", galleonChange)
        stickleChange = change % 493
    # to find the amount of change I have left after the galleons I used the modulus
    # the modulus provides the remainder (what's left over) after the galleon division
        stickles = stickleChange // 29
    # I used this division again to get an integer; I divided by 29 because there are 29 knuts in 1 stickles
        print("\tSickles:", stickles)
        knuts = stickleChange % 29
    # I am using the modulus again because I want to find out the remainder after the sickle division
    # the remainder is the amount of knuts the user will get in change
        print("\tKnuts:", knuts)
    # I am using the escape character \t to tab over the change to be more visually pleasing
main()