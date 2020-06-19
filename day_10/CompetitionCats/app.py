# CompetitionCats
#
# An application for competiting with cats!
from cat import Cat
import random

def new_cat(name):
    # let's get a name from the user
    print("Making a new cat!")
    sizes = ['small', 'medium', 'large']
    pride = random.randint(10, 25)
    energy = random.randint(15, 20)
    size = random.choice(sizes)
    cat = Cat(name, pride, energy, size)
    cat.save()

def find_cats():
    print("Finding a cat!")
    cats = Cat.get_all()
    return cats

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
            cats = find_cats()
            cat_name = input("which cat would you like to use?\n{}\n".format(cats))
            while (cat_name in cats) == False:
                print("{} was not found. Please select from the list: ".format(cat_name))
                cat_name = input("which cat would you like to use?\n{}\n".format(cats))

            cat = Cat.find_by_name(cat_name)
            print("You've chosen {}".format(cat.name))
        elif user_input == 'q':
            break
        else:
            user_input = input(menu)

run()