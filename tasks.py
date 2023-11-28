# Alex Palakian, palakian@usc.edu
# ITP 115, Spring 2022
# Section: 31836
# Final Project
# tasks.py
# Description: this file creates three functions that will be used to learn about the national parks. By directly working
# with the CSV file, this file sets the foundation. It creates a list of park dictionaries, a date conversion program, and
# a largest park determinator.

# parameters: the CSV file provided in the assignment; I set this as the default
# return: a list of dictionary objects where each park is its own dictionary
# this function loops through the CSV and uses the header values as the keys for every dictionary. Then, with a for loop,
# each park is examined and organized to assign values wit the respective keys
def readParksFile(fileName = "national_parks.csv"):
    parkList = []
    # empty list that will later be appended with dictionaries

    fileObject = open(fileName, "r")
    headerLine = fileObject.readline()
    word = headerLine.strip()
    headerWords = word.split(",")
    for park in fileObject:
        park = park.strip()
        nationalList = park.split(",")
        # opened the CVS file
        # used .readline() command to make the headers into a list
        # looped through each park and made them into a list

        for name in nationalList:
            name = {headerWords[0]: nationalList[0], headerWords[1]: nationalList[1], headerWords[2]: nationalList[2], headerWords[3]: nationalList[3],
                    headerWords[4]: nationalList[4], headerWords[5]: nationalList[5], headerWords[6]: nationalList[6], headerWords[7]: nationalList[7]}
            # for each park in the list of parks, I indexed the headers and each park list to assign a key and value correctly
        if name["Code"] not in parkList:
                parkList.append(name)
                # in order to not append the dict multiple times, I used the code value to monitor that only one type of park
                # for each park is appended to the empty list
    fileObject.close()
    # closed file
    return parkList

# parameters: a string with a date in this format: YYYY-MM-DD
# return: a string with a date in this format: Month Day, Year
# this function reorganizes the date and assigns values to certain numbers to return a qualitative date
def convertDate(dataStr):
    dataList = dataStr.split("-")
    # separating the dataStr by "-" to make a list
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    index = int(dataList[1])
    # dataList[1] is the month value which is a number
    monthValue = months[index - 1]
    # because indexing starts with 0, I needed to subtract by 1
    date = dataList[2]
    # day value
    year = dataList[0]
    # year value
    wordDate = monthValue + " " + date + "," + " " + year
    return wordDate

# parameters: list of parks where each park is a dictionary (from readParksFile())
# return: the park code (string) of the park with the largest area
# this function loops through each acre value and determines which one is the largest. From the value that is the largest,
# it gets the code of that park and returns it
def getLargestPark(parkList):
    size = 0
    index = 0
    number = 0
    # these are counters
    while index <= 55:
        # because there are 56 parks, it will loop through 56 times
        dictionary = parkList[index]
        # each time, it will take out a new park dict from the list and analyze it
        amount = int(dictionary["Acres"])
        # gets the value of "Acres" from each part, turn it into an int, and stores it
        if amount > size:
            size = amount
            number = index
            # if the "Acres" value is bigger that the size, the value will become the new size
            # if the "Acres" value is bigger that the size, its index will be stored
        index = index + 1
        # everytime this loops runs, 1 will be added

    codeDict = parkList[number]
    code = codeDict["Code"]
    # using the stored index, I can get the "Code" value of the "Acres" value
    return code