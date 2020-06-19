# CompetitionCats
#
# An application for competiting with cats!
from cat import Cat

def new_cat(name):
    # let's get a name from the user
    print("Making a new cat!")
    cat = Cat(name)
    cat.save()

def find_cat():
    print("Finding a cat!")

menu = '''
CompetitionCats!

Menu
n  make a new cat
u  use an existing cat
q  quit

What would you like to do?
'''

def run():
    while True:
        user_input = input(menu)
        if user_input == 'n':
            name = input("What is your cat's name? ")
            new_cat(name)
        elif user_input == 'u':
            find_cat()
        elif user_input == 'q':
            break
        else:
            user_input = input(menu)

run()