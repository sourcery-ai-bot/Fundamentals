# prompt a user to give their name, and assign it
# to the variable name.
first_name = input("What is your given name?\n")
last_name = input("What is your family name?\n")


# Interpolate the "name" variable into the greeting string
greeting = "Hello {family_name} {given_name}. It's nice to meet you.".format(given_name=first_name, family_name=last_name)
# greeting = "Hello {} {}. It's nice to meet you.".format(first_name, last_name)

# Print the greeting.
print(greeting)
