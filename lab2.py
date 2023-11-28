# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Lab 2

def main():
    year = int(input("Enter year: "))
    number = year % 12
    if number == 0:
        print(year, "is the Year of the Monkey.")
    elif number == 1:
        print(year, "is the Year of the Rooster.")
    elif number == 2:
        print(year, "is the Year of the Dog.")
    elif number == 3:
        print(year, "is the Year of the Pig.")
    elif number == 4:
        print(year, "is the Year of the Rat.")
    elif number == 5:
        print(year, "is the Year of the Ox.")
    elif number == 6:
        print(year, "is the Year of the Tiger.")
    elif number == 7:
        print(year, "is the Year of the Rabbit.")
    elif number == 8:
        print(year, "is the Year of the Dragon.")
    elif number == 9:
        print(year, "is the Year of the Snake.")
    elif number == 10:
        print(year, "is the Year of the Horse.")
    elif number == 11:
        print(year, "is the Year of the Goat.")
main()
