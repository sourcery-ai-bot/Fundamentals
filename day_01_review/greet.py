# Exercise 01
#
# Write a program that prompts a user for 
# their name, and then greets them.

# single name input
# name = input("What is your name?\n")
# print("Hello, {}! It's nice to meet you.".format(name))

# given name and family name
g_name = input("What is your given name?\n")
f_name = input("What is your family name?\n")

print("Hello, {given_name} {family_name}. It's nice to meet you!"
    .format(given_name=g_name, family_name=f_name))