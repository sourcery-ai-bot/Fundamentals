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
    return cat

def find_cats():
    print("Finding a cat!")
    return Cat.get_all()

def find_or_create(cat_name):
    cat = Cat.find_by_name(cat_name)
    if cat == '':
        return new_cat(cat_name)
    else:
        return cat

def determine_chance_to_win(cat):
    chance_to_win = 0

    if cat.size == 'medium':
        chance_to_win += 5
    elif cat.size == 'large':
        chance_to_win += 7
    else:
        chance_to_win += 3

    print("Cat Name: {}, Energy: {}".format(cat.name, type(cat.energy)))
    chance_to_win += cat.energy
    chance_to_win += cat.pride
    return chance_to_win

def playfight(comp, player):
    comp_chance = determine_chance_to_win(comp)
    player_chance = determine_chance_to_win(player)
    comp.energy -= 2
    player.energy -= 2
    if comp_chance == player_chance:
        print("It was a tie!")
    elif comp_chance > player_chance:
        print("{} wins!".format(comp.name))
        comp.energy += 3
        comp.pride += 1
    else:
        print("{} wins!".format(player.name))
        player.energy += 3
        player.pride += 1
    print("Here is the status of your cat:")
    print("Energy: {}, Pride: {}".format(player.energy, player.pride))


menu = '''
CompetitionCats!

Menu
n  make a new cat
u  use an existing cat
p  playfight
q  quit

What would you like to do?
'''

def run():
    global player_1
    global comp_1
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

            player_1 = Cat.find_by_name(cat_name)
            print("You've chosen {}".format(player_1.name))
        elif user_input == 'p':
            if player_1 == '':
                print("please select a cat first.")
            else:
                comp_1 = find_or_create('ComputerCat')
                print("Your cat is {}".format(player_1.name))
                print("Your opponent is {}".format(comp_1.name))
                playfight(comp_1, player_1)

        elif user_input == 'q':
            break
        else:
            user_input = input(menu)

run()