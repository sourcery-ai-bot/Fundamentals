class User:
    user_count = 0
    last_user_id = 0

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.name = "{} {}".format(first_name, last_name)
        User.user_count += 1
        User.last_user_id += 1
        self.id = User.last_user_id

    def get_user_count():
        return User.user_count
    # Class Method
    @classmethod

    def increment_user_id(cls, amount):
        cls.last_user_id += amount

# functions
userList = []
options = """
    q, quit     quit this program
    h, help     display this help menu
    v, view     view users
    a, add      add a user
    r, remove   remove a user
    """

def add_user(user):
    userList.append(user)

def view_list():
    if len(userList) != 0 :
        print("Here is usr list: ")
        print("Index \t ID \t User Name \t  eMail Address ")
        for user in userList:
            i = userList.index(user)
            print("{} \t {} \t {} \t {}".format(i, user.id, user.name, user.email))
    else:
        print("No user!!")

def remove_user(user):
    userList.remove(user)

def remove_user_by_id(id):
    index = -1
    for user in userList:
        index += 1
        if user.id == int(id):
            break
    if index == -1:
        print("Error : Non-existing ID")
    else:
        userList.pop(index)

def remove_user_by_index(i):
    userList.pop(i)

def welcome_user():
    print("Welcome to the user enrollment program")

def get_user_input(): 
    print(options)
    return input("\nEnter an option : ").lower()

def display_help():
    print(options)

# MAIN
welcome_user()
while True:
    user_choice = get_user_input()
    if user_choice in ["q", "quit"]:
        break
    elif user_choice in ["h", "help"]:
        display_help()
    elif user_choice in ["v", "view"]:
        view_list()
    elif user_choice in ["a", "add"]:
        first_name = input("Enter the first name : ")
        last_name = input("Enter the last name : ")
        email = input("Enter the e-mail address : ")
        new_user = User(first_name, last_name, email)
        add_user(new_user)
    elif user_choice in ["r", "remove"]:
        id = input("Enter the ID of the user to remove : ")
        remove_user_by_id(id)
