choice = input("What would you like to do? A: Eat Dinner, B: Go to a Movie?")

if choice not in ["A", "B"]:
    print("Choice must be A or B")
else:
    print("You chose {}".format(choice))