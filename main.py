from utils import get_file_contents, get_random_line

# Currently the main process, prints a joke OR fortune to the terminal :)
print("\n")
print("Welcome to Ye Olde Printer!\n")
print("Would you like to hear a JOKE, or receive a FORTUNE?\n")
input = str(input())

file_contents_list = []

if input == "JOKE":
    file_contents_list = get_file_contents("jokes")
elif input == "FORTUNE":
    file_contents_list = get_file_contents("fortunes")
elif input == "":
    input = "\" \""

if len(file_contents_list) > 0:
    print("\nBehold, your " + input + ":\n")
    print("------------------------------------------------------------------------------\n")
    print(get_random_line(file_contents_list))
    print("------------------------------------------------------------------------------\n")
else:
    print("Sorry, but " + input + " is not a valid command. Please try again.\n")

print("Thanks for using Ye Olde Printer!")
print("\n")
