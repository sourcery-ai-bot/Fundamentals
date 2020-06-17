# PlayFighting Cats App
#
# Create a program where two cats compete in a playfight for food.
#
# We need to create a couple of cats, some food, and a way to have a 
# playfight and determine who wins the food.
from food import Food
from cat import Cat


# Create some food
TheFood = Food()
print("TheFood energy_value is: {}".format(TheFood.energy_value))

# Create two cats that will playfight
sunny = Cat('Sunny the Cat', 16, 27, 'medium')
bob = Cat('Robert the Cat', 9, 30, 'large')

sunny.string()
bob.string()

# we have two cats, sunny and bob, who are competing in a 
# playfight for TheFood.
# 
# What are rules do we need for a playfight?

# We have energy, size, and pride as attributes for cats.
# Let's make some rules that determine who wins a playfight
# based on those attributes.

# What should those rules be?

def determine_chance_to_win(cat):
    chance_to_win = 0

    if cat.size == 'medium':
        chance_to_win += 5
    elif cat.size == 'large':
        chance_to_win += 7
    else:
        chance_to_win += 3

    chance_to_win += cat.energy
    chance_to_win += cat.pride
    return chance_to_win

sunny_chance_to_win = determine_chance_to_win(sunny)
bob_chance_to_win = determine_chance_to_win(bob)

if bob_chance_to_win == sunny_chance_to_win:
    print("It was a tie!")
elif bob_chance_to_win > sunny_chance_to_win:
    print("{} wins!".format(bob.name))
else:
    print("{} wins!".format(sunny.name))