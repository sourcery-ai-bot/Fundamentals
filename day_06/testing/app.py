# Exercises

# 1: write a funtion that takes a list as an argument, and returns the list reversed.
def reverse_list(list):
    reversed_list = []
    while len(list) > 0:        
        reversed_list.append(list.pop())

    return reversed_list

# 2: write a function that takes a country, and two lists (cities and populations) as arugments.
# it should return a dictionary whose key => value mappings are country => city. Cities should also
# be dictionaries of city => population.
def city_pop_dict(country, cities, populations):
    return_dictionary = {}
    return return_dictionary