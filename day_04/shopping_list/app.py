
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
    elif user_input in ["view list", "v"]:
        view_list()
    elif user_input == "a":
        item = input("Enter the name of an item: ")
        add_item(item)
    elif user_input == "r":
        item_index = int(input("Enter the number of the item to remove: "))
        remove_item_by_index(item_index)