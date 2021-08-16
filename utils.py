from random import randint
import subprocess

# Get the contents out of a .txt file and into a list
def get_file_contents(filename):
    our_file = open("resources/" + filename + ".txt", "r")
    content_list = our_file.readlines()
    our_file.close()
    return content_list

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
    jokelist = getfilecontentslist("oneliners")
    joketosend = getrandomjokefromlist(jokelist)
    stringbuild = "\n", "Time for a funny one-liner!", joketosend, "Thanks for using Ye Olde Printer!"
    glue = "\n"
    res = glue.join(stringbuild).encode('utf8')
    sendtoprinter(res)


def sendtoprinter(joke):
    print("Sending job to print queue...")
    print(joke)
    lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, close_fds=True)
    lpr.stdin.write(joke)
    lpr.stdin.flush()
    lpr.stdin.close()
