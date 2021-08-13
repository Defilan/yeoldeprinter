from random import randint

# Get the jokes out of a .txt file and into a list
def get_file_contents(filename):
    our_file = open("resources/" + filename + ".txt", "r")
    content_list = our_file.readlines()
    our_file.close()
    return content_list

# Choose a random joke from a given joke list
def get_random_joke(joke_list):
    return joke_list[randint(0, len(joke_list) - 1)]
