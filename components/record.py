from components import Name, Phone, Birthday
from utils import NumberIsNotFound

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        if phone_number in [p.value for p in self.phones]:
            print(f"Phone number {phone_number} already exists.")
            return
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        for phone in self.phones:
                if phone.value == phone_number:
                    self.phones.remove(phone)
                    break
        raise NumberIsNotFound()

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = Phone.validate_number(new_number)
                return "Phone updated."
        raise NumberIsNotFound()

    def find_phone(self, phone_number):
        for phone in self.phones:
                if phone.value == phone_number:
                    return phone
        raise NumberIsNotFound()

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def show_birthday(self):
        return self.birthday if self.birthday else "no information"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday if self.birthday else 'no information'}"

