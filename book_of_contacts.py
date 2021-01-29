import json
from pathlib import Path
import os


class Book_of_contacts():
    contact_list = []

    def add_contact(self):
        name = self.handle_letter_input("Name")
        surename = self.handle_letter_input("Surename")
        number = self.handle_numeric_input("Number")
        self.contact_list.append(
            {'name': name, 'surename': surename, "number": number})

    def handle_letter_input(self, field):
        while True:
            try:
                value = str(input(field+": "))
                if value.isalpha():
                    return value
                else:
                    raise TypeError
            except TypeError:
                print("Letters only please.")
                continue

    def handle_numeric_input(self, field):
        while True:
            try:
                value = int(input(field+": "))
                return value
            except ValueError:
                print("Digits only please.")
                continue

    def save(self):
        data = json.dumps(self.contact_list)
        filename = self.handle_letter_input("Saving, enter file name")
        Path(filename+'.json').write_text(data)

    def load(self, path):
        if os.path.isfile(Path(path)):
            data_recived = Path(path).read_text()
            self.contact_list = json.loads(data_recived)
        else:
            print("There no such path or file, write valide")

    def print_book(self):
        for contact in self.contact_list:
            print(contact.get("name"),
                  contact.get("surename"),
                  contact.get("number"))
