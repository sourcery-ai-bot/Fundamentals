# Command Line Interface
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
