class Cat:
    def __init__(self, name):
        self.name = name

    def save(self):
        cats_db = open('cats.db', 'a')
        cats_db.write(self.name + '\n')
        cats_db.close()

    @classmethod
    def get_all(cls):
        cats_db = open('cats.db', 'r')
        cats = []
        for cat in cats_db.readlines():
            cats.append(cat.strip('\n'))
        cats_db.close()
        return cats