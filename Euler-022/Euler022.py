#Answer: 871198282
import string

def main():

    #populate list with names in alphabetical order
    listOfNames = getListOfNames()

    #populate dictionary with value of each letter
    dictionary = {}
    populateDict(dictionary)

    #total of all the name scores in the file.
    totalScore = getTotalNameScore(listOfNames, dictionary)

    print(totalScore)

def getTotalNameScore(listOfNames, dictionary):
    total = 0
    index = 1
    for name in listOfNames:
        total += getNameScore(name, index, dictionary)
        index += 1
        
    return total

def getListOfNames():
    file = open("names.txt", 'r')
    listOfNames = file.read()
    file.close()    
    listOfNames = listOfNames.split(',')
    listOfNames.sort()
    
    return listOfNames

def populateDict(dictionary):
    dictionary['"'] = 0
    value = 1;
    
    for char in string.ascii_uppercase:
        dictionary[char] = value;
        value += 1;
            
def getNameScore(name, index, dictionary):
    total = 0
    for char in name:
        value = dictionary[char]
        total = total + value
        
    return total * index

main()
