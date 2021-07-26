class Cat:
    def __init__(self, name='', pride='', energy='', size=''):
        self.name = name
        self.pride = pride
        self.energy = energy
        self.size = size

    def save(self):
        with open('cats.db', 'a') as cats_db:
            cats_db.write("{}, {}, {}, {}\n".format(self.name, self.pride, self.energy, self.size))

    @classmethod
    def get_all(cls):
        with open('cats.db', 'r') as cats_db:
            cats = [cat.strip('\n').split(',')[0] for cat in cats_db.readlines()]
        return cats

    @classmethod
    def find_by_name(cls, name):
        cats_db = open('cats.db', 'r')
        found_cat = ''

        for cat in cats_db.readlines():
            # "Sheera, 20, 18, small\n"
            cat = cat.strip('\n').split(',')
            # ["Sheera", 20, 18, "small"]
            if cat[0] == name:
                found_cat = cls(cat[0], cat[1], cat[2], cat[3])
                print("found cat: {}, {}".format(found_cat.name, found_cat.energy))
            
        return found_cat