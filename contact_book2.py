
import sys
from book_of_contacts import Book_of_contacts


def add_contacts():
    book = Book_of_contacts()
    while True:
        book.add_contact()

        if input("Press enter for another record or type exit: ") == 'exit':
            break

    book.save()


def print_contacts(path):
    book = Book_of_contacts()
    book.load(path)
    book.print_book()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        add_contacts()
    else:
        print_contacts(sys.argv[1])
