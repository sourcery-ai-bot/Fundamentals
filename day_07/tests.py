from test_suite import TestSuite as test
from day_07 import *

def run_tests():
    # test reverse_list 01
    test_name = 'reverse_list 01'
    test_list = ['a', 'b', 'c', 'd']
    test.assert_equals(reverse_list(test_list), ['d', 'c', 'b', 'a'], test_name)

    # test reverse_list 02
    test_list = ['aa', 'bb', 'cc', 'dd']
    test.assert_equals(reverse_list(test_list), ['dd', 'cc', 'bb', 'aa'])

    # test reverse_list 03
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    test.assert_equals(reverse_list(test_list), [0, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    # test city_pop_dict 01
    country = "Russia"
    cities = ["Moscow", "Saint Petersburg", "Novosibirsk"]
    populations = [12432531, 5383890, 1618039]
    expected = {
        "Russia": {
            "Moscow": 12432531,
            "Saint Petersburg": 5383890,
            "Novosibirsk": 1618039
        }
    }
    test.assert_equals(city_pop_dict(country, cities, populations), expected)

run_tests()