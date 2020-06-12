from books import *
import os

TEST_DATA_FILE = 'test_books_data.text'

def assert_equals(actual, expected, test_name=""):
    if actual == expected:
        print("test {} passed!".format(test_name))
    else:
        print("FAILED: test {} failed.".format(test_name))
        print("Expected: {}".format(expected))
        print("Got: {}".format(actual))

def test_setup():
    print("Setting up")
    open(TEST_DATA_FILE, "a")

def test_teardown():
    print("Tearing down")
    os.remove(TEST_DATA_FILE)

def run_tests():
    test_setup()

    # test data
    expected = [
        {
            'author': 'Dr. Seuss', 
            'books': [
                'green eggs and ham', 
                'one fish two fish', 
                'the cat in the hat', 
                'horton hears a who'
            ]
        }, 
        {'author': 'J.K. Rowling', 'books': ['Harry Potter and something 1', 'Harry Potter and something 2']}, 
        {'author': 'Steven Pinker', 'books': ["The Language Instinct", "How the Mind Works", "Words and Rules"]},
        {'author': 'Dawkins', 'books': ["The Selfish Gene", "The Extended Phenotype", "The Blind Watchmaker"]}
    ]

    # add test data to data store
    for author_books in expected:
        add(author_books, TEST_DATA_FILE)
    
    # test that we can read the data that we added to the data store
    assert_equals(read(TEST_DATA_FILE), expected, "add authors to the data store")

    test_teardown()

run_tests()
