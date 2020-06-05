from app import reverse_list, city_pop_dict

def test_reverse_list_01():
    test_list = ['a', 'b', 'c', 'd']
    expected = ['d', 'c', 'b', 'a']
    actual = reverse_list(test_list)

    if actual == expected:
        print("test reverse list passed!")
    else:
        print("FAILED: test reverse list failed.")
        print("Expected: {}".format(expected))
        print("Got: {}".format(actual))

def test_reverse_list_02():
    test_list = ['aa', 'bb', 'cc', 'dd']
    expected = ['dd', 'cc', 'bb', 'aa']
    actual = reverse_list(test_list)

    if actual == expected:
        print("test reverse list passed!")
    else:
        print("FAILED: test reverse list failed.")
        print("Expected: {}".format(expected))
        print("Got: {}".format(actual))

def test_reverse_list_03():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    expected = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    actual = reverse_list(test_list)

    if actual == expected:
        print("test reverse list passed!")
    else:
        print("FAILED: test reverse list failed.")
        print("Expected: {}".format(expected))
        print("Got: {}".format(actual))

def test_city_pop_dict_01():
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

    actual = city_pop_dict(country, cities, populations)

    if actual == expected:
        print("test reverse list passed!")
    else:
        print("FAILED: test reverse list failed.")
        print("Expected: {}".format(expected))
        print("Got: {}".format(actual))
        

def run_tests():
    test_reverse_list_01()
    test_reverse_list_02()
    test_reverse_list_03()
    test_city_pop_dict_01()

run_tests()