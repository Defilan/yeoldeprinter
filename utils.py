from random import randint
import subprocess

# Get the contents out of a .txt file and return a list
def get_file_contents(filename):
    our_file = open("resources/" + filename + ".txt", "r")
    content_list = our_file.readlines()
    our_file.close()
    return content_list

# Returns a random item from a given list
def get_random_item(content_list):
    return content_list[randint(0, len(content_list) - 1)]

# Accept input and return a joke/fortune/error
def jokemaker(input):
    
    file_contents_list = []
    requestedContent = ""
    stringbuild = ""

    if input == "k":
        file_contents_list = get_file_contents("jokes")
        requestedContent = "joke"
    elif input == "j":
        file_contents_list = get_file_contents("fortunes")
        requestedContent = "fortune"
    elif input == "":
        input = "\" \""

    output = get_random_item(file_contents_list)

    if len(file_contents_list) > 0:
        stringbuild = "\n", "Time for a" + requestedContent + "!", output, "Thanks for using Ye Olde Printer!"
    else:
        stringbuild = "\n", "Sorry, but " + input + " is not a valid command. Please try again."

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