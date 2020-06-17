class Cat():
    def __init__(self, name, energy, pride, size):
        self.name = name
        self.energy = energy
        self.pride = pride
        self.size = size

    def eat(self, food):
        print("{} is eating {} for {} energy!".format(self.name, food.food_type, food.energy_value))
        self.energy += food.energy_value

    def string(self):
        print("name: {}, energy: {}, pride: {}, size: {}".format(self.name, self.energy, self.pride, self.size))
