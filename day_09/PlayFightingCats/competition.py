class Competition:
    def __init__(self, cat_1, cat_2):
        self.cat_1 = cat_1
        self.cat_2 = cat_2

    def determine_chance_to_win(self, cat):
        chance_to_win = 0

        if cat.size == 'medium':
            chance_to_win += 5
        elif cat.size == 'large':
            chance_to_win += 7
        else:
            chance_to_win += 3

        chance_to_win += cat.energy
        chance_to_win += cat.pride
        return chance_to_win

    def playfight(self, prize):
        print("Starting playfight between {} and {}".format(self.cat_1.name, self.cat_2.name))
        self.cat_status()
        cat_1_chance_to_win = self.determine_chance_to_win(self.cat_1)
        cat_2_chance_to_win = self.determine_chance_to_win(self.cat_2)
        self.cat_1.energy -= 2
        self.cat_2.energy -= 2
        if cat_1_chance_to_win == cat_2_chance_to_win:
            print("It was a tie!")
        elif cat_1_chance_to_win > cat_2_chance_to_win:
            print("{} wins!".format(self.cat_1.name))
            self.cat_1.eat(prize)
            self.cat_1.pride += 1
        else:
            print("{} wins!".format(self.cat_2.name))
            self.cat_2.eat(prize)
            self.cat_2.pride += 1
        self.cat_status()
        
    def cat_status(self):
        self.cat_1.string()
        self.cat_2.string()