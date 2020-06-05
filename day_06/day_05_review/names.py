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

def get_names_list():
    names = []
    names_file = open('names_file', 'r')
    for name in names_file:
        names.append(name.strip('\n'))
    return names

def view_names_with_index():
    names = get_names_list()
    for name in names:
        print("{}: {}".format(names.index(name), name))

def find_name_by_index(name_index):
    names = get_names_list()
    return names[name_index]

def update(name, new_name):
    names = get_names_list()
    name_index = names.index(name) # 0
    names[name_index] = new_name
    
    my_file = open('names_file', 'w')
    for name in names:
        my_file.write(name + '\n')
