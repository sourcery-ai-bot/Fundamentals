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

## Exercise 03:

Let's think back to the homework we did on day 02. We thought about an application that would be able to handle lists of authors and their books.

```python
# Write a program that asks a user what the user wants to do. The choices are:
# view authors, view books by author, add authors, add books to authors.
help_menu = """
OUR WONDERFUL LIST OF BOOKS -- HELP MENU
========================================

COMMANDS              DESCRIPTION
--------              -----------

h, help               prints this help menu
view authors          view a list of all the authors
view books by author  view a list of books, organized by author
add authors           add authors by name
add books to authors  add books to authors by name of author and title of book
q, quit               quits the program
"""

while True:
    choice = input("What do you want to do? (Type 'help' for the help menu): ")

    if choice == "help" or choice == 'h':
        print(help_menu)
    elif choice == "q" or choice == "quit":
        break
    elif choice == "view authors":
        print("You chose {}.".format(choice))
    elif choice == "view books by author":
        print("You chose {}.".format(choice))
    elif choice == "add authors":
        print("You chose {}.".format(choice))
    elif choice == "add books to authors":
        print("You chose {}.".format(choice))
    else:
        print("ERROR: Invalid selection!")
        print(help_menu)
```

What might the data look like? How might we store it? What might it look like in memory, and what might it look like on disk (i.e. in a file)?

```python
list_of_books = ['green eggs and ham', 'one fish two fish', 'the cat in the hat', 'horton hears and who']
author = 'Dr. Seuss'

authors_and_books = {author: list_of_books}

authors_and_books = {
    'Dr. Seuss': ['green eggs and ham', 'one fish two fish', 'the cat in the hat', 'horton hears and who'],
    'J.K. Rowling': ['Harry Potter and something 1', 'Harry Potter and something 2']
}

for author in authors_and_books:
    print("Author: " + author)
    print("Books: {}".format(authors_and_books[author]))


```

Another way we could store authors and books is in a list of key, value dictionaries, i.e.
```python
authors_and_books = [
    {'author': 'Dr. Seuss', 'books': ['green eggs and ham', 'one fish two fish', 'the cat in the hat', 'horton hears and who']}, 
    {'author': 'J.K. Rowling', 'books': ['Harry Potter and something 1', 'Harry Potter and something 2']}, 
    {'author': 'Steven Pinker', 'books': ["The Language Instinct", "How the Mind Works", "Words and Rules"]}
]

for item in authors_and_books:
    print("{}'s books include: ".format(item[author], item[books]))

```

Now, let's think a little about what a file that stores this data might look like.

```txt
Dr. Seuss, green eggs and ham, one fish two fish, the cat in the hat, horton hears and who
J.K. Rowling, Harry Potter and something 1, Harry Potter and something 2
Steven Pinker, The Language Instinct, How the Mind Works, Words and Rules

```

Having spent some time thinking through the way we might store data in memory and on disk, let's think through some of the functions we might need to create and use this data. While doing so, let's keep our help menu in mind

```python
help_menu = """
OUR WONDERFUL LIST OF BOOKS -- HELP MENU
========================================

COMMANDS              DESCRIPTION
--------              -----------

h, help               prints this help menu
view authors          view a list of all the authors
view books by author  view a list of books, organized by author
add authors           add authors by name
add books to authors  add books to authors by name of author and title of book
q, quit               quits the program
"""

```

a.) Write function that will read data from the data storage (in this case a file). But, before you do, write a test.

```python
def read():
    # your code goes here
    pass

```

b.) Write a function that will write data _to_ the data storage. But, before you do, write a test.

```python
def write():
    # your code goes here
    pass

```
