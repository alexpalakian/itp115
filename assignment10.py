# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Assignment 10
# Description: this program will allow the user to interact with a music library by allowing them to insert, update, and
#              delete data from the library (dictionary) using a series of functions

import MusicLibraryHelper
import random
# I imported these two commands and function from external sources to use in my program

def displayMenu():
    print("Manage Your Music Library")
    print("\ta) Display library")
    print("\tb) Display artists")
    print("\tc) Add an artist/album")
    print("\td) Delete an album")
    print("\te) Delete an artist")
    print("\tf) Generate a random playlist")
    print("\tg) Exit")
    # parameters: none
    # return: none
    # this purpose of this function is to print the display menu as a side effect
    # I utilized \t to tab over the options


def displayLibrary(dictionary):
    for key in dictionary:
        print("Artist:", key)
        print("\tAlbums:")
        value = dictionary[key]
        for i in range(len(value)):
            print("\t\t", value[i])
    # parameters: a dictionary representing the music library
    # return: none
    # this function loops through each key (artist) and assess the information
    # in order to print the artists with many albums (value in the dictionary), and because the values are in a list,
    # I add another for loop to get a number based on the length of that list and printed each album using the index
    # overall, this function displays the music library in the wanted format


def displayArtists(dictionary):
    print("Artists:")
    for key in dictionary:
        print("\t" + key)
    # parameters: a dictionary representing the music library
    # return: none
    # similar to the displayLibrary(), I looped through each key (artist) in the dictionary and printed
    # out each artist to display all the artists in the music library


def addAlbum(dictionary):
    userArtist = input("Enter artist: ")
    userAlbum = input("Enter album: ")
    artist = userArtist.title()
    album = userAlbum.title()
    if artist in dictionary:
        if album not in dictionary[artist]:
            dictionary[artist].append(album)
    else:
        dictionary[artist] = [album]
    # parameters: a dictionary representing the music library
    # return: none
    # this function asks the user to enter the album they want to add to the library by asking the artist and specific album
    # I employed .title() to capitalize their answers
    # I used branching to see if the album was in the dictionary or not as another from an existing artist or new one
    # because the album value is a list, a simply appended the value if the artist existed
    # if not, I made the album a list by splitting the string and then added the key and value to the dictionary


def deleteAlbum(dictionary):
    userArtist = input("Enter artist: ")
    userAlbum = input("Enter album: ")
    artist = userArtist.title()
    album = userAlbum.title()
    if artist in dictionary or album in dictionary:
        value = dictionary[artist]
        value.remove(album)
        return True
    else:
        return False
    # parameter: a dictionary representing the music library
    # return: a boolean value to determine if the album was successfully deleted or not
    # this function asks the user to enter the album they want to delete from the library by asking the artist and specific album
    # I employed .title() to capitalize their answers
    # I used branching to determine of the artist and album they want to delete is in the dictionary; if it is, I stored
    # the values in the dictionary into a variable that is a list. To the list I .remove() with the user's chosen album as the value
    # to delete the album from the library --> True is returned
    # if the artist and album is not in the dictionary, the program cannot delete the album because it is not in the dictionary
    # thus, nothing is done --> False is returned


def deleteArtist(dictionary):
    userArtist = input("Enter artist: ")
    artist = userArtist.title()
    if artist in dictionary:
        del dictionary[artist]
        return True
    else:
        return False
    # parameter: a dictionary representing the music library
    # return: a boolean value to determine if the artist was successfully deleted
    # the function similarly asks the user to enter an artist they want to delete and capitalizes the input
    # I used branching to determine if the artist was in the dictionary
    # if they were, I used the dict command of del dict[key] to delete that section in the dictionary all together --> True is returned
    # if not, nothing happens because the artist is not in the list --> False is returned


def generateRandomPlaylist(dictionary):
    print("Here is your random playlist:")
    for key in dictionary:
        value = dictionary[key]
        print("\t", random.choice(value), "by", key)
    # parameter: a dictionary representing the music library
    # return: none
    # this function randomly selects one album from every artist in the library and displays the selection to the user via a side effect
    # to do so, I looped through each artist in the dictionary, assignment the values of the artist into a variable that
    # is a list and applied the random.choice() to the value to randomly chose an album


def main():
    dictionary = MusicLibraryHelper.loadLibrary("music_library.dat")
    # this value holds the dictionary that was created from the MusicLibraryHelper.loadLibrary() that transcribed
    # the "music_library.dat" file
    displayMenu()
    # this code calls the function and displays its side effect
    choice = input("Choice: ")
    userChoice = choice.lower()
    # this code asks the user to pick their choice based on the displayMenu(). I also made their choice not case-sensitive
    while userChoice != "g":
        # this is a while loop that will run so long as the user's choice is not "g"
        if userChoice != "a" and userChoice != "b" and userChoice != "c" and userChoice != "d" and userChoice != "e" and userChoice != "f":
            print("Invalid entry")
            # if the user choice is not a-f, then the program will print a statement about invalidity
        elif userChoice == "a":
            displayLibrary(dictionary)
            # if the user choice is "a", the program will call the displayLibrary() function and use the dictionary variable as the input
        elif userChoice == "b":
            displayArtists(dictionary)
            # if the user choice is "b", the program will call  the displayArtist() function and use the dictionary variable as the input
        elif userChoice == "c":
            addAlbum(dictionary)
            # if the user choice is "c", the program will call the addAlbum() function and use the dictionary variable as the input
        elif userChoice == "d":
            albumValue = deleteAlbum(dictionary)
            if albumValue == True:
                print("Delete album success")
            else:
                print("Delete album failed")
                # if the user choice is "d", the program will call the deleteAlbum() function and use the dictionary variable as the input
                # the return value is stored in a variable and through branching, will print the appropriate message
        elif userChoice == "e":
            artistValue = deleteArtist(dictionary)
            if artistValue == True:
                print("Delete artist success")
            else:
                print("Delete artist failed")
                # if the user choice is "d", the program will call the deleteArtist() function and use the dictionary variable as the input
                # the return value is stored in a variable and through branching, will print the appropriate message
        elif userChoice == "f":
            generateRandomPlaylist(dictionary)
            # if the user choice is "f", the program will call the generateRandomPlaylist() function and use the dictionary variable as the input
        print()
        # space
        displayMenu()
        choice = input("Choice: ")
        userChoice = choice.lower()
        # after branching the loop will display the menu again and ask the user to enter another choice...

    userFile = input("Enter music library filename: ")
    MusicLibraryHelper.saveLibrary("music_library.dat", userFile)
    print("Saved music library to", userFile)
    # if the user choice is "g", the while loop will stop and the above code will happen:
    # ask the user to enter a filename and uses the filename to write the information into the file using the imported function
    # parameters: none
    # return: none
    # the main() function organizes the other functions based on the user choice

main()
