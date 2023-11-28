# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Lab 3

def main():
    print("What would you like to know?")
    print("a) Favorite Animal")
    print("f) Favorite Food")
    print("p) Favorite place")
    print("q) Quit")
    choice = input("> ")
    while choice.lower() != "q":
        if choice.lower() == "a":
            print("My favorite animal is a cow.")
        elif choice.lower() == "f":
            print("My favorite food is coffee (I consider it a food).")
        elif choice.lower() == "p":
            print("My favorite place is New York City.")
        else:
            print("That option is not available.")
        print()
        print("What would you like to know?")
        print("a) Favorite Animal")
        print("f) Favorite Food")
        print("p) Favorite place")
        print("q) Quit")
        choice = input("> ")
    print("Goodbye")
main()