# Fundamentals Day 04  

Today, we are going to review some of the concepts that we have introduced, and expand upon them.

## Data Types

An `int` is a whole number. 1, 164, 6999 are integers. The range supported by the int type is -2147483648 through 2147483647.

A `float` or a floating point number has a decimal. 1.1, 3.14, 68.126123123 are floats.

A `str` or string is something wrapped in quotes. In python we can use single quotes or double quotes interchangably, as long as we are consistent. 

Examples:

```python
# assign int values to two variables, a and b:
a = 1
b = 2

# some operations we can perform on integers are:
a + b
b * 3
c = b / a

# we can interpolate the value of variables in strings.
# Let's do it!
favorite_candy = "Skittles"

"Allan's favorite candy is {}.".format(favorite_candy)

# we can also concatenate strings using the
# concatenation operator.

"Allan's favorite candy is" + " " + favorite_candy + "."
```

## Functions

Functions are great for allowing us to do something repeatedly. We can define a thing, or things that need to be done, and group them together using functions.

Examples:

```python
def prepare_greeting(name):
    return "Hello {}! It's nice to see you!".format(name)

def get_name():
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    return first_name + " " + last_name

def greet():
    name = get_name()
    greeting = prepare_greeting(name)
    print(greeting)

greet()

# variadic parameters
def list_names(*names):
    for name in names:
        print("Hello " + name +"!")
```

## Data Structures

A list `[]` can be filled with items of any type, and we can iterate over the list, or do many other things with it. There are several built in methods that can be called on lists. We can also create our own functions for working with them.

## Exercise 01

Let's create a shopping list. I should be able to add items to the list, and then remove them from the list after I buy them (or add them to a cart).

```python

# SHOPPING LIST
# 
# Assumptions: 
#   - There is only 1 list
#   - It is either empty or has items
#   - You can add items to the list
#   - You can remove items from the list

# LIST OPERATIONS
# ===============
list = []

def add_item(item):
    list.append(item)

def view_list():
    print("Here is your shopping list: ")
    for item in list:
        i = list.index(item)
        print("{}: {}".format(i, item))

def remove_item(item):
    list.remove(item)

def remove_item_by_index(item_index):
    list.pop(item_index)


# USER INTERACTION
# ================

# let's prompt a user with a list of options.
# Options
#   - View list
#   - Add item to list
#   - Remove item from list

options = ["View list: v", "Add item to list: a", "Remove item from list: r", "Quit: q"]

def welcome_user():
    print("Welcome to the list program!\n")

def show_options():
    print("The options are: ")
    for option in options:
        print(" - " + option)

def get_user_input():
    return input("\nEnter an option: ").lower()
    
welcome_user()

while True:
    show_options()
    user_input = get_user_input()
    if user_input == "q":
        break
    elif user_input == "view list" or user_input == "v":
        view_list()
    elif user_input == "a":
        item = input("Enter the name of an item: ")
        add_item(item)
    elif user_input == "r":
        item_index = int(input("Enter the number of the item to remove: "))
        remove_item_by_index(item_index)
```

## Classes

Classes & instances... if you think about a Class as a blueprint for an object, you can use it to create many objects of the same type. For example, we could create user objects, box objects, book objects, and so on.

```python
class User:
    user_count = 0
    last_user_id = 0

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        User.user_count += 1
        User.last_user_id += 1
        self.id = User.last_user_id

    def name(self):
         return "{} {}".format(self.first_name, self.last_name)

    # to create a class method, add a decorator
    @classmethod
    def increment_user_id(cls, amount):
        cls.last_user_id += amount

```

## Exercise 02

Let's create a program that allows you to add, remove, and view users. Use the Shopping List program, and the `User` class as your guide.

```python

```