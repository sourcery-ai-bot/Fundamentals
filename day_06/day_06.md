# Fundamentals Day 06  

## Day 05 Review - Exercise 02

a.) Write a program that prompts the user to enter their name. The program should allow you to enter your name or view all entries. It should also store the names in a file.

b.) Next, add the ability to update a name (by index).

```python
# Python Application
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

options = """
q  quit
a  add name
v  view names

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
    else:
        print("That option is not supported")    

# names file

Drew
Emily
Jackson
Jason


```