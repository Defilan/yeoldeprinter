import os
import subprocess
from utils import getFileContentsList, getRandomJokeFromList


# def quotemaker():
#     return "This is a funny joke"
#
#
# file = open("/tmp/example.txt", "w")
# file.write("This is funny")
# print(file.read("/tmp/example.txt"))
# file.close()

# sender = "This is a test of the program"


# lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
# lpr.stdin.write(b"Printing from Python!")

print("\n")
print("Time for a funny one-liner!\n")
jokeList = getFileContentsList("oneliners")
print(getRandomJokeFromList(jokeList))
print("Thanks for using Ye Olde Printer!")
print("\n")