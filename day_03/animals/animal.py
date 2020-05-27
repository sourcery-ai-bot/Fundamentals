class Animal():
    # constructor
    def __init__(self, lol='unknown', f='unknown', g='unknown'):
        self.species = lol
        self.food = f
        self.greeting = g

    def introduce(self):
        print("I am a {}.".format(self.species))

    def eat(self):
        print("I eat {}.".format(self.food))

    def speak(self):
        print("{}".format(self.greeting))


a = Animal("tiger", "meat", "rawr!")

a.introduce()
a.eat()
a.speak()

b = Animal("chicken", "grain", "bawk!")
b.introduce()
b.eat()
b.speak()