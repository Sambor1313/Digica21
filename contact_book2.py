import argparse
import io
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--saved_contacts",
                        help="path to save json file",
                        type=argparse.FileType('r'))
    args = parser.parse_args()

    if not args.saved_contacts:
        add_contacts()
    else:
        # print(args.saved_contacts)
        print_contacts(args.saved_contacts)
