# Write a program that asks a user what the user wants to do. The choices are:
# view authors, view books by author, add authors, add books to authors.
help_menu = """
OUR WONDERFUL LIST OF BOOKS -- HELP MENU
========================================

COMMANDS              DESCRIPTION
--------              -----------

h, help               prints this help menu
view authors          view a list of all the authors
view books by author  view a list of books, organized by author
add authors           add authors by name
add books to authors  add books to authors by name of author and title of book
q, quit               quits the program
"""

choice = input("What do you want to do? (Type 'help' for the help menu): ")

if choice == "help" or choice == 'h':
    print(help_menu)
elif choice == "view authors":
    print("You chose {}.".format(choice))
elif choice == "view books by author":
    print("You chose {}.".format(choice))
elif choice == "add authors":
    print("You chose {}.".format(choice))
elif choice == "add books to authors":
    print("You chose {}.".format(choice))
else:
    print("Invalid selection.")
    print(help_menu)