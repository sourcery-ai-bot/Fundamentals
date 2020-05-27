# Fundamentals Day 03  
  
Today, we are going to talk about Classes. We will also discuss words (and their meanings) such as _instance_, _object_, _namespace_.  

Let's define a class called `Person`, with a single attribute `name` that has a default value of `'unknown'`:

```python
# define the class
class Person():
    name = 'unknown'

# create some instances of the class
p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()
p5 = Person()

# give each person a name
p1 = 'Jackson'
p2 = 'Allan'
p3 = 'Emily'
p4 = 'Alex'
p5 = 'Jason'

# make a list of people
people = [p1, p2, p3, p4, p5]

# iterate through the list, and print
# each person's name
for person in people:
    print(person.name)

```

## Exercise 01

Create a class `Bird` with a `size` attribute. Then instantiate 3 (or more) instances of birds, each with a different size.

```python

class Bird():
    size = ''

sparrow = Bird()
chicken = Bird()
eagle = Bird()

sparrow.size = 'small'
chicken.size = 'medium'
eagle.size = 'large'

```

We can also pass in arguments at the time of instantiating an object. To do this, we use Python objects' `__init__` method.

```python
class Animal():
    def __init__(self, species):
        self.species = species



tweety = Animal("canary")

tweety.species
```

Looking at how we defined the `Animal` class, rewrite the `Bird` class to take an argument of `size` upon instantiation.

```python

class Bird():
    def __init__(self, size='small'):
        self.size = size

crow = Bird()
humming = Bird()
eagle = Bird()
crow.size = "small"
humming.size = "medium"
eagle.size = "large"

```

Let's imagine that `Animal` is a very generic type of class that most living creatures belong to. What are some common characteristics or behaviors among all (or most) animals?

```python
class Animal():
    # constructor
    def __init__(self, lol='unknown', f='unknown', g='unknown'):
        self.species = lol
        self.food = f
        self.greeting = g

    def introduce(self):
        print("I am a {}.".format(self.species))

    def eat(self):
        print("I eat {}.".format(self.food))

    def speak(self):
        print("{}".format(self.greeting))


a = Animal("tiger", "meat", "rawr!")

a.introduce()
a.eat()
a.speak()

b = Animal("chicken", "grain", "bawk!")
b.introduce()
b.eat()
b.speak()

```

Now, use the example `Animal` class and instances and create some more instances of animals!

## Exercise 02

Looking at the example of `Animal`, think about how we would use classes to create users for an application. What attributes and methods might be important?

Create a `User` class.

```python
class User():
    def __init__(self, first_name, last_name, email_address, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.password = password

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

```

What if we have something like a bag, and in the bag there are items? How might we make something like that work? 

```python
class Bag():
    def __init__(self, size):
        self.items = []
        self.size = size

    def add(self, item):
        self.items.append(item)

```

Often, we will put a class into its own file. In this case, if we have a file `bag.py` for the `Bag` class, a file `item.py` for the `Item` class, and an `app.py` file that runs our program, we can import the classes, if the files are in the same directory by calling `from <filename> import <classname>`.

```python
# bag.py
class Bag():
    def __init__(self, size):
        self.items = []
        self.size = size

    def put(self, item):
        #print("putting item ({}) into bag.".format(item.name))
        self.items.append(item)

    def remove(self):
        item = self.items.pop()
        #print("removing item ({})...".format(item.name))

    def look_inside(self):
        # if there are no items in my bag, I would like to
        # print "the bag is empty"
        if len(self.items) == 0:
            print("The bag is empty")
            return
        else:
            for item in self.items:
                print(item.name)

```
```python
# item.py
class Item():
    def __init__(self, name, size):
        self.name = name
        self.size = size

```

```python
# app.py
from bag import Bag
from item import Item

# create some items
item1 = Item("candy", 1)
item2 = Item("pencil", 1)
item3 = Item("umbrella", 3)
item4 = Item("book", 2)

# create a bag
back_pack1 = Bag(10)

# put the items in the bag
back_pack1.put(item1)
back_pack1.put(item2)
back_pack1.put(item3)
back_pack1.put(item4)

# look inside the bag
back_pack1.look_inside()

# remove the items
back_pack1.remove()
back_pack1.remove()
back_pack1.remove()
back_pack1.remove()

# look inside the bag
back_pack1.look_inside()

```
