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
