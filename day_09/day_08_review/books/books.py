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
