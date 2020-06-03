
def get_user_name():
    # prompt a user to give their name.
    name = input("What is your name? ")
    return name

def save(name):
    # write the name to a file
    names = open('names', 'a')
    names.write(name + '\n')

def show_names():
    names = open('names', 'r')
    names_list = names.readlines()
    for name in names_list:
        print("{} {}".format(names_list.index(name), name), end='')

def update_name():
    print("TODO: Implement me!")

def remove_name(name_index):
    print("TODO: Implement me!")

options = '''
NAMES
=====

Help Menu

q           quit
v           view names
a           add name
e           edit name
r           remove name
'''

def get_user_input():
    return input("Enter an option: ").lower()

while True:
    print(options)
    user_input = get_user_input()
    if user_input == "q":
        break
    elif user_input == "v":
        show_names()
    elif user_input == "a":
        name = get_user_name()
        save(name)
    elif user_input == "e":
        update_name()
    elif user_input == "r":
        name_index = int(input("Enter the number of the name to remove: "))
        remove_name(name_index)
