def reverse_list(list):
    reversed_list = []
    while len(list) > 0:        
        reversed_list.append(list.pop())

    return reversed_list

def city_pop_dict(country, cities, populations):
    city_pops = {city: populations[cities.index(city)] for city in cities}
    return {country: city_pops}