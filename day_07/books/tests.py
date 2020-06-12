from books import *

def assert_equals(actual, expected, test_name=""):
    if actual == expected:
        print("test {} passed!".format(test_name))
    else:
        print("FAILED: test {} failed.".format(test_name))
        print("Expected: {}".format(expected))
        print("Got: {}".format(actual))

def run_tests():
    # test read authors from data store
    expected = [
        {'author': 'Dr. Seuss', 'books': ['green eggs and ham', 'one fish two fish', 'the cat in the hat', 'horton hears and who']}, 
        {'author': 'J.K. Rowling', 'books': ['Harry Potter and something 1', 'Harry Potter and something 2']}, 
        {'author': 'Steven Pinker', 'books': ["The Language Instinct", "How the Mind Works", "Words and Rules"]}
    ]
    assert_equals(read(), expected, "read authors and books from the data store")


    test add author to data store
    expected = [
        {'author': 'Dr. Seuss', 'books': ['green eggs and ham', 'one fish two fish', 'the cat in the hat', 'horton hears and who']}, 
        {'author': 'J.K. Rowling', 'books': ['Harry Potter and something 1', 'Harry Potter and something 2']}, 
        {'author': 'Steven Pinker', 'books': ["The Language Instinct", "How the Mind Works", "Words and Rules"]},
        {'author': 'Dawkins', 'books': ["The Selfish Gene", "The Extended Phenotype", "The Blind Watchmaker"]}
    ]
    author = {'author': 'Dawkins', 'books': ["The Selfish Gene", "The Extended Phenotype", "The Blind Watchmaker"]}
    add(author)
    assert_equals(read(), expected, "add author to the data store")

run_tests()
