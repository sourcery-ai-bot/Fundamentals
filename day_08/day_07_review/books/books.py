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
    # 1.) open a file so that we can write to it

    # 2.) author = {'author': 'Dawkins', 'books': ["The Selfish Gene", "The Extended Phenotype", "The Blind Watchmaker"]}
    # format the author dictionary into a string that looks like what our file wants, i.e.
    # author_and_books = 'Dawkins, The Selfish Gene, The Extended Phenotype, The Blind Watchmaker'
    # then we want to write that author_and_books item to the books_data.txt file.