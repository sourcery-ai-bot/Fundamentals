# def prepare_greeting(name):
#     return "Hello {}! It's nice to see you!".format(name)

# def get_name():
#     first_name = input("What is your first name?")
#     last_name = input("What is your last name?")
#     return first_name + " " + last_name

# def greet():
#     name = get_name()
#     greeting = prepare_greeting(name)
#     print(greeting)

# def list_names(*names):
#     for name in names:
#         print("Hello " + name +"!")

# list_names("Drew", "Charles", "Jackson", "Jason", "Allan", "Emily")

def greet(name):
    print("Hello {}!".format(name))

greeting = greet("Drew")