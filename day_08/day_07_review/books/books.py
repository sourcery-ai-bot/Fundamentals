def read(filename='books_data.txt'):
    with open(filename, 'r') as file:
        data_list = file.readlines()
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

def add(author, filename='books_data.txt'):
    with open(filename, 'a') as file:
        author_and_books = author['author']
        for book in author['books']:
            author_and_books += ', ' + book

        file.write(author_and_books + '\n')
