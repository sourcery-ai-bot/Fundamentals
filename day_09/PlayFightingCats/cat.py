class Cat():
    def __init__(self, name, energy, pride, size):
        self.name = name
        self.energy = energy
        self.pride = pride
        self.size = size

    def string(self):
        print("name: {}, energy: {}, pride: {}, size: {}".format(self.name, self.energy, self.pride, self.size))
        