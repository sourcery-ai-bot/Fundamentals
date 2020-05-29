# Let's create a program that allows you 
# to add, remove, and view users. Use the 
# Shopping List program, and the `User` class 
# as your guide.

# USERS APPLICATION
# 
# Assumptions:
#   - users are instances of the User class
#   - users will be stored in a list
#   - viewing users will display user full names
#   - adding users will require all the required arguments
#     for creating a user (first name, last name, email)
#   - the user interface is the terminal

# USER OPERATIONS
# ===============

# END USER INTERACTION
# ====================

# Prompt an application user with a list of options.
# Options
#   - view users
#   - add a user
#   - remove a user

options = """
USERS
==================================

q, quit    quit this program
h, help    display this help menu
v, view    view users
a, add     add a user
r, remove  remove a user
"""

def get_user_input():
    user_input = input("Enter a command: ")
    return user_input

def run_program():
    print(options)
    
    while True:
        user_input = get_user_input()
        if user_input == "q" or user_input == "quit":
            break
        elif user_input == "h" or user_input == "help":
            print(options)
        else:
            print("Unrecognized command: {}".format(user_input))
            print(options)    
     
run_program()
