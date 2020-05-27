class Bag():
    def __init__(self, size):
        self.items = []
        self.size = size

    def put(self, item):
        #print("putting item ({}) into bag.".format(item.name))
        self.items.append(item)

    def remove(self):
        item = self.items.pop()
        #print("removing item ({})...".format(item.name))

    def look_inside(self):
        # if there are no items in my bag, I would like to
        # print "the bag is empty"
        if len(self.items) == 0:
            print("The bag is empty")
            return
        else:
            for item in self.items:
                print(item.name)
        
