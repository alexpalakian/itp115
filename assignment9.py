# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Assignment 9
# Description: using functions and a CSV file of 14 languages and its equivalent english words, this code is a language
#              translator program that allows the user to choose a language and an english word, and the program will
#              display the translation while writing the results into a file

def getAllLanguages(fileName = "languages.csv"):
    fileObject = open(fileName, "r")
    for line in fileObject:
        line = line.strip()
        headerWords = line.split(",")
        fileObject.close()
        return headerWords
    # parameters: the CSV file which has a default of "languages.csv"
    # return: a list of strings that contain the header row (list of language options)
    # this function opens the CSV file and runs through the lines, getting rid of the spaces and separating each string
    # with a comma to form a list

def getTranslationLanguage(languagesList):
    listWithoutEnglish = languagesList[1:]
    print("Translate English words to one of the following languages: \n", listWithoutEnglish)
    userLanguage = input("Enter a language: ")
    while userLanguage.capitalize() not in listWithoutEnglish:
        print("This program does not support", userLanguage.capitalize())
        userLanguage = input("Enter a language: ")
    return userLanguage.capitalize()
    # parameters: list of languages (this will eventually be inputted from the getAllLanguages() function return value)
    # return: string of the langauge the user wants to translate english words into
    # this function first removes english from the language option by slicing english out
    # it then prints out the non-english languages and asks the user to enter a language--using a while loop
    # to make sure the user language is a part of the list
    # I make sure to use capitalize() command to capitalize the first letter of the language to make it identifiable with the list

def readDataFile(languagesList, languageStr = "English", fileName = "languages.csv"):
    userLanguage = languageStr
    wordsList = []
    fileObject = open(fileName, "r")
    headerLine = fileObject.readline()
    index = languagesList.index(userLanguage)
    for line in fileObject:
        line = line.strip()
        lineList = line.split(",")
        words = lineList[index]
        wordsList.append(words)
    fileObject.close()
    return wordsList
    # parameter: list of languages (this will eventually be inputted from the getAllLanguages() function return value)
    # parameter: string containing the name of the user language (set to a default of "english")
    # parameter: CSV file (set to a default of "languages.csv")
    # return: list of words of the language from the LanguageStr value
    # this function opens the "languages.csv" and ignores the header line through the readline() function
    # it also indexes the list of languages with the value of the language of the languageStr to store a number (the index number)
    # the function then loops through each line in the file a picks out the word that matches the index position, and appends
    # all of those for each line in the wordsList

def createTextFile(language):
    languageFile = language.capitalize() + ".txt"
    fileObject = open(languageFile, "w")
    print("Words translated from English to", language, file=fileObject)
    fileObject.close()
    # parameter: the user language for translation
    # return: none
    # this function creates a new file name of (language).txt
    # this function creates and opens the new file to write, printing a statement of what the english words are being
    # translated into

def transalteWords(englishList, translationList, language):
    yesOrNo = "y"
    while yesOrNo.lower() == "y":
    # I created a do while loop to ask the user if they want to translate another word after trying it once
        languageFile = language.capitalize() + ".txt"
        fileObject = open(languageFile, "a")
        print()
        # this code opens the same file created in createTextFile() function and allows information to be added (appended)
        english = input("Enter a word to translate: ")
        if english not in englishList:
            print(english, "is not in the English list")
            # this code asks the user to enter an english word they would like to translate and error checks if the word
            # is a part of the list of english words. If not the program will print such statement
        else:
        # if the english word is in the english list...
            index = englishList.index(english)
            translatedWord = translationList[index]
            # similar to what I did in the readDataFile() function, I indexed the english list with the english word to find
            # the position of the word in the list. I stored the number in the index variable to find the translated word
            # that is in the same position using the list of words in the desired langauge
            if translatedWord == "-":
                print(english, "did not have a translation")
            else:
                print(english, "is translated to", translatedWord)
                print(english, "=", translatedWord, file=fileObject)
            # using branching, if there is not a equivalent translated word, I printed a message
            # if there is, I printed the translated word and appended that information into my created file
        yesOrNo = input("Another word (y or n)? ")
        # I asked the user if they want to continue; if yes the loop will run again; if not the program will print a message
    print()
    print("Translated words have been saved to the", languageFile)
    fileObject.close()
    # parameters: list of english words, list of words in the desired language, the user (desired) language
    # return: none
    # this function essentially in the translator program, using the lists I created to find the translated word

def main():
    print("Language Translator")
    headerWords = getAllLanguages()
    englishWords = readDataFile(headerWords)
    userLanguage = getTranslationLanguage(headerWords)
    translationWords = readDataFile(headerWords, userLanguage)
    createTextFile(userLanguage)
    transalteWords(englishWords, translationWords, userLanguage)
    # parameters: none
    # return: none
    # this function calls all functions previously created and pieces everything together
    # is stores the return values into variables and uses those variables as respective inputs

main()
















