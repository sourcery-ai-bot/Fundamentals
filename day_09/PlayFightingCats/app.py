# PlayFighting Cats App
#
# Create a program where two cats compete in a playfight for food.
#
# We need to create a couple of cats, some food, and a way to have a 
# playfight and determine who wins the food.
from food import Food
from cat import Cat
from competition import Competition


# Create some food
prize_food = Food()
print("TheFood energy_value is: {}".format(prize_food.energy_value))

# Create two cats that will playfight
sunny = Cat('Sunny the Cat', 16, 27, 'medium')
bob = Cat('Robert the Cat', 9, 30, 'large')

sunny.string()
bob.string()

sunny.eat(prize_food)
bob.eat(prize_food)



# we have two cats, sunny and bob, who are competing in a 
# playfight for TheFood.
# 
# What are rules do we need for a playfight?

# We have energy, size, and pride as attributes for cats.
# Let's make some rules that determine who wins a playfight
# based on those attributes.

# What should those rules be?

competition1 = Competition(sunny, bob)
competition1.playfight()

