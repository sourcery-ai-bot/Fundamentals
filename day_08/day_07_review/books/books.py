def read():
    file = open('books_data.txt', 'r')
    data_list = file.readlines()
    file.close()

    books_and_authors = []
    for item in data_list:
        item = item.strip('\n')
        data_entry = item.split(',')
        author = data_entry.pop(0)
        books = []
        for book in data_entry:
            book = book.strip()
            books.append(book)
        books_and_authors.append({'author': author, 'books': books})


    return books_and_authors

def add(author):
    file = open('books_data.txt', 'a')
    author_and_books = author['author']
    for book in author['books']:
        author_and_books += ', ' + book

    file.write('\n' + author_and_books)
    file.close()
