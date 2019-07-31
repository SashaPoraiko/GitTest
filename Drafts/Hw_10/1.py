import file_modules

commands = ['end', 'write', 'read', 'calculate']


def read(file_name):
    print(file_modules.read(file_name))


def write(file_name):
    inc_book = input('Enter the Book: ')
    if not validate(inc_book.split('\t')):
        print('Wrong data!')
        return
    file_modules.write(file_name, inc_book)


def calculate_unique_authors(file_name):
    books_list = file_modules.listing(file_name)
    unique_authors = []
    for book in filter(lambda x: x[0] not in unique_authors, books_list):
        unique_authors.append(book[0])
    return unique_authors


def calculate_oldest_book(file_name):
    books_list = file_modules.listing(file_name)
    oldest_book = books_list[0]
    

def validate(data):
    return len(data) == 6


def run():
    file = 'books.txt'
    while True:

        command = input('Enter the command: ')
        if command == 'end':
            break
        if command not in commands:
            print('Wrong command! ')
            continue

        if command == 'write':
            write(file)
        elif command == 'read':
            read(file)
        elif command == 'calculate':
            print(1)


if __name__ == '__main__':
    run()
