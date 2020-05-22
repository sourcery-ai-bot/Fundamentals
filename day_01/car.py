# a = 5
# if a > 15:
#     print("Big number!")
# elif a > 10:
#     print("Medium number!")
# else:
#     print("Small number!")


## Exercise 04

# Write code that asks users for the year 
# of their car and then prints: future, new, 
# old or very old, depending on the year.

year = input("What year is your car?")
car_year = int(year)
if car_year > 2020:
    reaction = "Wow!"
    description = "from the future"
elif car_year >= 2015:
    reaction = "Cool!"
    description = "new"
elif car_year > 2010: 
    reaction = "OK."
    description = "old"
else:
    reaction = "Umm." 
    description = "very old"

print("{} Your car is {}.".format(reaction, description))





