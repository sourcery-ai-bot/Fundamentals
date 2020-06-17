def read(filename='books_data'):
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

def add(author, filename='books_data.txt'):
  file = open(filename, "a")
  author_and_books = author["author"]
  books = author['books']
  for book in books:
    author_and_books += ", " + book
  file.write(author_and_books + '\n')
  file.close()
