# Fundamentals Day 07  

## Exercise 01:
Look at this example code. It shows how we would translate the test cases on codewars into test cases in our familiar syntax.

```python
@test.describe('Example Tests')
def example_tests():
    #test_state_capitals_01
    state_capitals = [{'state': 'Maine', 'capital': 'Augusta'}]
    test.assert_equals(capital(state_capitals), ["The capital of Maine is Augusta"]);

    state_capitals = [{'state': 'Maine', 'capital': 'Augusta'}]
    actual = capital(state_capitals)
    expected = ["The capital of Maine is Augusta"]
    test.assert_equals(actual, expected)


    country_capitals = [{'country' : 'Spain', 'capital' : 'Madrid'}]
    test.assert_equals(capital(country_capitals), ["The capital of Spain is Madrid"])
    #test.assert_equals(actual, expected)
    
    mixed_capitals = [{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}]
    test.assert_equals(capital(mixed_capitals), ["The capital of Maine is Augusta", "The capital of Spain is Madrid"]]
    

def test_state_capitals_01():
    state_capitals = [{'state': 'Maine', 'capital': 'Augusta'}]
    expected = ["The capital of Maine is Augusta"]
    actual = capital(country_capitals)

    if actual == expected:
        print("test reverse list passed!")
    else:
        print("FAILED: test reverse list failed.")
        print("Expected: {}".format(expected))
        print("Got: {}".format(actual))
```
Use this example to do the opposite. That is, rewrite one of our test cases into codewars syntax:
```python
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
```

```python
def example_tests():
    test_list = ['a', 'b', 'c', 'd']
    test.assert_equals(reverse_list(test_list), ['d', 'c', 'b', 'a'])

def example_tests():
    test_list = ['a', 'b', 'c', 'd']
    expected = ['d', 'c', 'b', 'a']
    actual = reverse_list(test_list)
    test.assert_equals(actual, expected)
```

We can implement our own test suite _framework_ following this method signature. For example, we can create a file called `test_suite.py` with a class `TestSuite` and a method `assert_equals` that takes two arguments: `actual` and `expected`. It then compares to two. If they are equal, the tests pass. If they are not, the tests fail.
```python
# test_suite.py
class TestSuite():
    def assert_equals(actual, expected):
        if actual == expected:
            print("test passed!")
        else:
            print("FAILED: test failed.")
            print("Expected: {}".format(expected))
            print("Got: {}".format(actual))
```

We can then import that `TestSuite` as `test` (or as `TestSuite` if we do not specify `as <something>`), and call it from our tests:

```python
# tests.py
from test_suite import TestSuite as test
from day_07 import *

def run_tests():
    test_list = ['a', 'b', 'c', 'd']
    test.assert_equals(reverse_list(test_list), ['d', 'c', 'b', 'a'])

run_tests()
```
And of course we have our function `reverse_list` to test:

```python
# day_07.py
def reverse_list(list):
    reversed_list = []
    while len(list) > 0:        
        reversed_list.append(list.pop())

    return reversed_list

```

## Exercise 02:

Using our new test suite framework, refactor the rest of the tests from day 06.