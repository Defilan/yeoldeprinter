from random import randint

# Get the jokes out of a .txt file and into a list
def getFileContentsList(filename):
    file = open("resources/" + filename + ".txt", "r")
    contentList = file.readlines()
    file.close()
    return contentList

def getRandomJokeFromList(jokeList):
    return jokeList[randint(0, len(jokeList))]