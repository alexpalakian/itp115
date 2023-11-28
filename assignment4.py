# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Assignment 4
# Description: This code will allow the user to enter multiple sets of numbers, and determine the smallest
#              number, the largest number, and the average. There will also be a stop feature.
def main():

    userContinue = "y"
    # I am setting this variable to 'y' to automatically run the code without asking
    while userContinue.lower() == "y":
    # here, I am establishing a do while, outer loop
    # the outer loop will control the whole program repeating (y/n) question; if y then the program will run the inner loop
    # the do while loop will run the code, and then check the condition (reverse from a while loop)
    # this is why the the userContinue question comes after the code and not before
    # I set the do while loop equal to y (yes) allowing the inner loop to run again; if it is anything other than y, the
    # outer loop will stop and print whatever is after the loop, in this case "goodbye!"
    # .lower() is so the code is not case sensitive; the user can enter lowercase and uppercase

        small = 9999999999
        large = 0
        numCount = 0
        sum = 0
        avg = 0
        userNum = 0
    # these variables hold integers all equal to 0 expect for 'small' because nothing can be smaller than 0 in this case and
    # 999999 is the most inclusive number
        print("Input an integer greater than or equal to 0 or -1 to quit: ")
    # this will print the string above

        while userNum != -1:
            userChoice = int(input("> "))
    # this is the beginning of my inner loop, the 'heart' of the code
    # while loops allow code to repeat
    # in order for it not to be an infinite loop, it ends when the user enters a sentinel value of -1.
    # userChoice allows the user to enter a number
            while userChoice < -1:
                userChoice = int(input("Error: Input an integer greater than or equal to 0 or -1 to quit:> "))
    # I decided to error check in case the user entered a value less than -1, which is not allowed
            if int(userChoice) > large:
                large = int(userChoice)
            elif int(userChoice) < small and int(userChoice) != -1:
                small = int(userChoice)
    # these if and elif statements allow the set of numbers to be defined by the smallest and largest value
    # every value the user inputs, it will run through these statements and replace the previous value it is less
    # than or greater than, respectively (starting from the assigned value of 0)
            numCount = numCount + 1
    # I am adding 1 because the numCount starts at 0 (the assigned value)
            sum = sum + int(userChoice)
    # because the sum is set to 0, I add the sum to every userChoice allowing the sum to get bigger with more values
            userNum = int(userChoice)
    # every value the user enters becomes distinctive userNums

            if int(userChoice) == -1:
    # because I have the sentinel value of -1, this indicates that the inner loop will stop and everything after will print
                numCount = numCount - 1
    # I am subtracting from 1 to counteract the -1 value to not take that into account for the total numbers
                sum = sum + 1
    # I added 1 to the sum to balance out the -1; -1 + 1 = 0
                print("The largest number is", str(large))
                print("The smallest number is", str(small))
    # I converted the integers to a string value so it would be outputted
                avg = sum / numCount
                print("The average number is", str(avg))
    # the average is the sum divided by the total number count; I used // to get a float value (with decimals) so the
    # average is more accurate
    # when I printed it, I converted the avg to a string so it would be outputted.
                print()
                # spacing

        userContinue = input("Would you like to enter another set of number (y/n)?: ")
    # because it is a for while loop, the outer loop will run its condition (the statement above), after it runs the code
    # I am changing the variable from 'y' to user input so the user can now decide
        print()
        #spacing

    print("Goodbye!")
    # we do not need an else statement in a while loop because if the action isn't happening the code won't run
    # this will print when the user enters anything other than y/Y when asked--ending the outer loop and overall code

main()