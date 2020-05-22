def get_name(which):
    return input("What is your {} name?\n".format(which))

first_name = get_name("given")
last_name = get_name("family")

def greet(fname, gname):
    greeting = "Hello {family_name} {given_name}. It's nice to meet you.".format(given_name=fname, family_name=gname)
    print(greeting)

greet(first_name, last_name)