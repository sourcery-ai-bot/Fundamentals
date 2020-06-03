
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
    for name in names:
        print(name, end='')

name = get_user_name()
save(name)
show_names()

