from action_decorator import action_error
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def validate_phone(self):
        if not self.value.isdigit() or len(str(self.value)) != 10:
            raise ValueError("Phone number should contain 10 digits")


class Record:
    def __init__(self, record_name):
        self.name = Name(record_name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        phone_obj.validate_phone()
        self.phones.append(phone_obj)

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value


class AddressBook(UserDict):
    def add_record(self, new_record):
        self.data[new_record.name.value] = new_record

    @action_error
    def find(self, search_name):
        return self.data[search_name]

    @action_error
    def delete(self, search_name):
        del self.data[search_name]


book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")

book.add_record(jane_record)


for name, record in book.data.items():
    print(record)

john = book.find("John")
print(john)
john.edit_phone("1234567890", "1112223333")

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

book.delete("Jane")
