from books import add, read
import os

TEST_DATA_FILE='test_books_data.txt'

def assert_equals(actual, expected, test_name=""):
    if actual == expected:
        print("test {} passed!".format(test_name))
    else:
        print("FAILED: test {} failed.".format(test_name))
        print("Expected: {}".format(expected))
        print("Got: {}".format(actual))

def setup_tests():
    # create a file for storing test data, if it does not exist.
    print("Setting up tests...")
    open(TEST_DATA_FILE, 'a')

def teardown_tests():
    os.remove(TEST_DATA_FILE)
    print("Tearing down tests...")

def run_tests():
    # prepare some test data
    test_data = [
        {'author': 'Dr. Seuss', 'books': ['green eggs and ham', 'one fish two fish', 'the cat in the hat', 'horton hears and who']}, 
        {'author': 'J.K. Rowling', 'books': ['Harry Potter and something 1', 'Harry Potter and something 2']}, 
        {'author': 'Steven Pinker', 'books': ["The Language Instinct", "How the Mind Works", "Words and Rules"]},
        {'author': 'Dawkins', 'books': ["The Selfish Gene", "The Extended Phenotype", "The Blind Watchmaker"]}
    ]

    # add the test data
    for author in test_data:
        add(author, TEST_DATA_FILE)

    expected = [
        {'author': 'Dr. Seuss', 'books': ['green eggs and ham', 'one fish two fish', 'the cat in the hat', 'horton hears and who']}, 
        {'author': 'J.K. Rowling', 'books': ['Harry Potter and something 1', 'Harry Potter and something 2']}, 
        {'author': 'Steven Pinker', 'books': ["The Language Instinct", "How the Mind Works", "Words and Rules"]},
        {'author': 'Dawkins', 'books': ["The Selfish Gene", "The Extended Phenotype", "The Blind Watchmaker"]}
    ]

    # test that the test data was written to the test data store
    assert_equals(read(TEST_DATA_FILE), expected, "adds and reads authors")

setup_tests()
run_tests()
teardown_tests()
