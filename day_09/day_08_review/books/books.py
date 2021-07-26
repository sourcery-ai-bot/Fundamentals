def read(filename='books_data'):
  with open(filename, 'r') as file:
    data_list = file.readlines()
  authors_books = []
  for book_info in data_list:
    author_books = {}
    book_info = book_info.strip('\n')
    book_list = book_info.split(',')
    books = []
    for i, item in enumerate(book_list):
      if i == 0:
          author = item
      else:
          books.append(item.strip())
    author_books['author'] = author
    author_books['books'] = books
    authors_books.append(author_books)

  return authors_books

def add(author, filename='books_data.txt'):
  with open(filename, "a") as file:
    author_and_books = author["author"]
    books = author['books']
    for book in books:
      author_and_books += ", " + book
    file.write(author_and_books + '\n')
