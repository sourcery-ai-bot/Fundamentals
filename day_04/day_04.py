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

# def greet(name):
#     print("Hello {}!".format(name))

# greeting = greet("Drew")

class User:
    user_count = 0
    last_user_id = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = last_name + "@example.com"
        User.user_count += 1
        User.last_user_id += 1
        self.id = User.last_user_id

    def name(self):
         return "{} {}".format(self.first_name, self.last_name)

    # to create a class method, add a decorator
    @classmethod
    def increment_user_id(cls, amount):
        cls.last_user_id += amount


    
u1 = User("Sam", "Stone", "sam@example.com")
u2 = User("Cloe", "Smith", "cloe@example.com")

print(u1.name(), u1.id)
print(u2.name(), u2.id)

User.increment_user_id(50)

u3 = User("Clarence", "Golden", "clarence@example.com")

print(u3.name(), u3.id)

