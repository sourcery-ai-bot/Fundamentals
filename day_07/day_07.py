
# Exercise 01:
# Look at this example code. It shows how we would translate the test cases on
# codewars into test cases in our familiar syntax.

@test.describe('Example Tests')
def example_tests():
    state_capitals = [{'state': 'Maine', 'capital': 'Augusta'}]
    test.assert_equals(capital(state_capitals), ["The capital of Maine is Augusta"]);
    
    country_capitals = [{'country' : 'Spain', 'capital' : 'Madrid'}]
    test.assert_equals(capital(country_capitals), ["The capital of Spain is Madrid"])
    
    mixed_capitals = [{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}]
    test.assert_equals(capital(mixed_capitals), ["The capital of M
    

def test_city_pop_dict_01():
    state_capitals = [{'state': 'Maine', 'capital': 'Augusta'}]
    expected = ["The capital of Maine is Augusta"]
    actual = capital(country_capitals)

    if actual == expected:
        print("test reverse list passed!")
    else:
        print("FAILED: test reverse list failed.")
        print("Expected: {}".format(expected))
        print("Got: {}".format(actual))

# Use this example to do the opposite. That is, rewrite one of our test cases into
# codewars syntax:
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

@test.describe('test reverse list 01')
def example_tests():
    # Your answer goes here
    pass
