from utils import get_file_contents, get_random_joke

# Currently the main process, prints a joke to the terminal :)
print("\n")
print("Time for a funny one-liner!\n")
joke_list = get_file_contents("oneliners")
print(get_random_joke(joke_list))
print("Thanks for using Ye Olde Printer!")
print("\n")
