class Cat:
    def __init__(self, name='', pride='', energy='', size=''):
        self.name = name
        self.pride = pride
        self.energy = energy
        self.size = size

    def save(self):
        cats_db = open('cats.db', 'a')
        cats_db.write("{}, {}, {}, {}\n".format(self.name, self.pride, self.energy, self.size))
        cats_db.close()

    @classmethod
    def get_all(cls):
        cats_db = open('cats.db', 'r')
        cats = []
        for cat in cats_db.readlines():
            # this_cat = cat.strip('\n')
            # # 'Plushy, 12, 32, large'
            # this_cat = this_cat.split(',')
            # # ['Plushy', 12, 32, 'large']
            # this_cat = this_cat[0]
            # cats.append(this_cat)
            cats.append(cat.strip('\n').split(',')[0])
            
        cats_db.close()
        return cats

    @classmethod
    def find_by_name(cls, name):
        cats_db = open('cats.db', 'r')
        found_cat = ''

        for cat in cats_db.readlines():
            # "Sheera, 20, 18, small\n"
            cat = cat.strip('\n').split(',')
            # ["Sheera", "20", "18", "small"]
            if cat[0] == name:
                found_cat = cls(cat[0], int(cat[1]), int(cat[2]), cat[3])
                print("found cat: {}, {}".format(found_cat.name, found_cat.energy))
            
        return found_cat