# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Lab 9

def readFile(userGenre, fileName):
    fileObject = open(fileName, "r")
    shows = []
    for line in fileObject:
        line = line.strip()
        lineList = line.split(",")
        showGenre = lineList[1]
        if userGenre in showGenre:
            showName = lineList[0]
            shows.append(showName)
    fileObject.close()
    return shows

def writeFile(genre, showList):
    fileObject = open(genre + ".txt", "w")
    for show in showList:
        print(show, file=fileObject)
    fileObject.close()

def main():
    print("TV Shows")
    genres = "action & adventure, animation, comedy,\ndocumentary, drama, mystery & suspense, science fiction & fantasy"
    print("Possible genres are", genres)
    userGenre = input("Enter a genre: ")
    while userGenre not in genres:
        userGenre = input("Enter a genre: ")
    tvShows = readFile(userGenre, "shows.csv")
    writeFile(userGenre, tvShows)
    print("The file \'" + userGenre + ".txt\' has the following shows:")
    print(tvShows)

main()