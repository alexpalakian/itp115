# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Lab 1
def main():
    print("\"Do your little bit of good where you are; it's those little bits of good put together that overwhelm the world.\" - Desmond Tutu")
    # quotations within a string will not result in an output, this is implement the special character: \" to do so
    # I expect this string to be outputted in quotes with the author at the end
    week = input("Enter the day of the week: ")
    month = input("Enter the month: ")
    # the use of input is to ask the user to type information that can later be stored
    # here, these two messages are displayed to the user and their answers (values) will be assigned to such variables
    date = int(input("Enter the day: "))
    # input must always be a string, because this message will result in an integer value, int(input() needs to be added
    print()
    # the () above is to output an empty line for separation
    print("Today is " + week + ", " + month, date)
    # by concatenating a string with variables, a message will be outputted with the stored values of the user
    print("Tomorrow will be", month, str(date + 1) + ".")
    # because a string and an integer cannot be outputted together, I had to make this operation a str by adding str()
main()