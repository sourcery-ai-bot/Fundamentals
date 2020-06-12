def read():
    file = open('books_data.txt', 'r')
    data_list = file.readlines()
    file.close()

    books_and_authors = []
    for item in data_list:
        data_entry = item.split(',')
        author = data_entry.pop(0)
        books = data_entry
        books_and_authors.append({'author': author, 'books': books})


    return books_and_authors

def add(author):
    pass