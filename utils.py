from random import randint


# Get the jokes out of a .txt file and into a list
def getfilecontentslist(filename):
    ourfile = open("resources/" + filename + ".txt", "r")
    contentlist = ourfile.readlines()
    ourfile.close()
    return contentlist


# Choose a random joke from a given joke list
def getrandomjokefromlist(jokelist):
    return jokelist[randint(0, len(jokelist) - 1)]


def jokemaker():
    print("\n")
    print("Time for a funny one-liner!\n")
    jokelist = getfilecontentslist("oneliners")
    print(getrandomjokefromlist(jokelist))
    print("Thanks for using Ye Olde Printer!")
    print("\n")
