from utils import getfilecontentslist, getrandomjokefromlist

print("\n")
print("Time for a funny one-liner!\n")
jokeList = getfilecontentslist("oneliners")
print(getrandomjokefromlist(jokeList))
print("Thanks for using Ye Olde Printer!")
print("\n")
