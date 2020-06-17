# Fundamentals Day 09

In the last module, we worked on some tests for our books application. Let's review where we left off, and finish the tasks we set out to accomplish.

## Day 08 Review

a.) Add some functionality to the `test_setup` function to:
    - create a test data file
    - possibly add some data to it

b.) Add some functionality to the `test_teardown` function to:
    - remove the test data file

**HINT**: have a look at the [os](https://docs.python.org/3.8/library/os.html) library.

We had 3 files we were working with: `tests.py` for the tests, `books.py` our main application logic, and `books_data.txt` for storing records of books.  
  
[Day 08 Exercise 02](https://repl.it/@DrewOgryzek/Day08Exercise02)  
  
```python
# tests.py
from books import add, read

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

    # test add author to data store
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

```

```python
# books.py
def read():
  filename = "books_data.txt"
  file = open(filename, 'r')
  data_list = file.readlines()
  file.close()
  authors_books = []
  for book_info in data_list:
    author_books = {}
    book_info = book_info.strip('\n')
    book_list = book_info.split(',')
    i = 0
    books = []
    for item in book_list:
      if i == 0:
          author = item
      else:
          books.append(item.strip())
      i += 1
    author_books['author'] = author
    author_books['books'] = books
    authors_books.append(author_books)

  return authors_books

def add(author):
  file = open("books_data.txt", "a")
  author_and_books = author["author"]
  books = author['books']
  for book in books:
    author_and_books += ", " + book
  file.write('\n' + author_and_books)
  file.close()

```

`books_data.txt`:
```txt
Dr. Seuss, green eggs and ham, one fish two fish, the cat in the hat, horton hears and who
J.K. Rowling, Harry Potter and something 1, Harry Potter and something 2
Steven Pinker, The Language Instinct, How the Mind Works, Words and Rules
```