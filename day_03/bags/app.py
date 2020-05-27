from bag import Bag
from item import Item

# create some items
item1 = Item("candy", 1)
item2 = Item("pencil", 1)
item3 = Item("umbrella", 3)
item4 = Item("book", 2)

# create a bag
back_pack1 = Bag(10)

# put the items in the bag
back_pack1.put(item1)
back_pack1.put(item2)
back_pack1.put(item3)
back_pack1.put(item4)

# look inside the bag
back_pack1.look_inside()

# remove the items
back_pack1.remove()
back_pack1.remove()
back_pack1.remove()
back_pack1.remove()

# look inside the bag
back_pack1.look_inside()