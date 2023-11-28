# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Lab 10

def readFile(fileName):
    letterDict = {}
    fileObject = open(fileName, "r")
    for line in fileObject:
        line = line.strip()
        for character in line:
            character = character.lower()
            if character.isalpha():
                if character not in letterDict:
                    letterDict[character] = 1
                else:
                    letterDict[character] = letterDict[character] + 1
    fileObject.close()
    return letterDict

def sortKeys(dictionary):
    keysList = list(dictionary.keys())
    keysList.sort()
    return keysList

def main():
    dictionary = readFile("speech.txt")
    sortedKeysList = sortKeys(dictionary)
    print("The frequency of letters are:")
    for key in sortedKeysList:
        value = dictionary[key]
        print(key, ":", value)

main()