from random import randint
import subprocess


# Get the contents out of a .txt file and return a list
def get_file_contents(filename, isstring):
    our_file = open("resources/" + filename + ".txt", "r")
    if isstring:
        content_list = our_file.read()
    else:
        content_list = our_file.readlines()
    our_file.close()
    return content_list


# Returns a random item from a given list
def get_random_item(content_list):
    return content_list[randint(0, len(content_list) - 1)]


# Accept input and return a joke/fortune/error
def jokemaker(inputparam):
    file_contents_list = []
    requestedcontent = ""
    stringbuild = ""

    if inputparam == "k":
        file_contents_list = get_file_contents("jokes", False)
        requestedcontent = "joke"
    elif inputparam == "j":
        file_contents_list = get_file_contents("fortunes", False)
        requestedcontent = "fortune"

    output = get_random_item(file_contents_list)
    yeolde = get_file_contents("yeolde", True)
    if len(file_contents_list) > 0:
        stringbuild = yeolde, "\n", "Time for a " + requestedcontent + "!", output, "Thanks for using Ye Olde Printer!"
    else:
        stringbuild = "\n", "Sorry, but " + inputparam + " is not a valid command. Please try again."

    glue = "\n"
    res = glue.join(stringbuild).encode('utf8')
    sendtoprinter(res)


def sendtoprinter(output):
    print("Sending job to print queue...")
    print(output)
    lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, close_fds=True)
    lpr.stdin.write(output)
    lpr.stdin.flush()
    lpr.stdin.close()
