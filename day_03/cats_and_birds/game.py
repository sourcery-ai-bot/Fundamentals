from cat import Cat
from bag import Bag
from bird import Bird

# create a cat
print("Creating an instance of a cat")
cat1 = Cat("Felix")

print("The cat's name is {}.".format(cat1.name))

# create a bag
print("Creating an instance of a bag")
bag1 = Bag(10)
print("The bag's size is {}.".format(bag1.size))

# create a bird
print("Creating an instance of a bird")
bird1 = Bird("Foghorn Leghorn", 5)
print("The bird's name is {}, and its size is {}".format(bird1.name, bird1.size))