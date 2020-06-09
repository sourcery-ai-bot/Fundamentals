# Fundamentals Day 06  

## Day 05 Review - Exercise 02

a.) Write a program that prompts the user to enter their name. The program should allow you to enter your name or view all entries. It should also store the names in a file.

b.) Next, add the ability to update a name (by index).

```python
# Python Application

# names.py
def get_name():
    name = input("What is your name?\n")
    return name

def get_names(number=10):
    names = []
    while number > 0:
        names.append(get_name() + "\n")
        number -= 1

    return names

def save(names):
    names_file = open('names_file', 'a')
    for name in names:
        names_file.write(name)

def view_names():
    names_file = open('names_file', 'r')
    for name in names_file:
        print(name, end='')

def get_names_list():
    names = []
    names_file = open('names_file', 'r')
    for name in names_file:
        names.append(name.strip('\n'))
    return names

def view_names_with_index():
    names = get_names_list()
    for name in names:
        print("{}: {}".format(names.index(name), name))

def find_name_by_index(name_index):
    names = get_names_list()
    return names[name_index]

def update(name, new_name):
    names = get_names_list()
    name_index = names.index(name) # 0
    names[name_index] = new_name
    
    my_file = open('names_file', 'w')
    for name in names:
        my_file.write(name + '\n')
  
# Command Line Interface
# cli.py
from names import *

options = """
q  quit
a  add name
v  view names
e  edit name

What would you like to do?
"""

while True:
    user_input = input(options)
    if user_input == "q":
        break
    elif user_input == "a":
        name = get_names(1)
        save(name)
    elif user_input == "v":
        view_names()
    elif user_input == "e":
        view_names_with_index()
        name_index = int(input("Enter which number you'd like to edit: "))
        name = find_name_by_index(name_index)
        new_name = input("What should {}'s new name be?".format(name))
        update(name, new_name)
    else:
        print("That option is not supported")


# names file
Drew
Emily
Jackson
Jason
```

## Testing

