from random import randint

# Get the contents out of a .txt file and into a list
def get_file_contents(filename):
    our_file = open("resources/" + filename + ".txt", "r")
    content_list = our_file.readlines()
    our_file.close()
    return content_list

# Choose a random line from a given list
def get_random_line(input_list):
    return input_list[randint(0, len(input_list) - 1)]
