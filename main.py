from components import Record, AddressBook

from utils import *

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError):
            error_messages = {
                "add_contact": "Give me name and phone please.",
                "change_contact": "Give me name, old phone, and new phone please.",
                "show_phone": "Give me name please.",
                "add_birthday": "Give me name please and birthday date.",
                "show_birthday": "Give me name please.",
            }
            return error_messages.get(func.__name__, "Missing required parameters.")
        except KeyError:
            return "Contact is not found."
        except NumberIsNotFound:
            return "Number is not found."           
        except InvalidValue as e:
            return str(e)

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if not record:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)

    if record:
        record.edit_phone(old_phone, new_phone)
        return "Contact changed."

    raise KeyError()


@input_error
def show_phone(args, book):
    (name,) = args
    record = book.find(name)
    if record is None:
        raise KeyError()
    return f"{record}"


def show_all(book):
    return (
        "\n".join(str(record) for record in book.data.values())
        if book.data
        else "No contacts found."
    )


@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if record:
        message = "Birthday added."
        if record.birthday:
            message = "Birthday updated."
        record.add_birthday(birthday)
        return message
    raise KeyError()


@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        return record.show_birthday()
    else:
        raise KeyError()


def birthdays(_, book):
    upcoming = book.get_upcoming_birthdays()
    if isinstance(upcoming, str):
        return upcoming
    return [f"{birthday['name']} - {birthday['congratulation_date']}" for birthday in upcoming]


def show_commands():
    commands = [
        "hello",
        "add [name] [phone]",
        "change [name] [old phone] [new phone]",
        "phone [name]",
        "all",
        "add-birthday [name] [DD.MM.YYYY]",
        "show-birthday [name]",
        "birthdays",
        "commands",
        "close or exit",
    ]
    return "Available commands:\n 👉 " + "\n 👉 ".join(commands)


def main():
    book = load_data()
    print("Welcome to the assistant bot!🤖")
    print(show_commands())
    while True:
        user_input = input("Enter a command:")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        elif command == "commands":
            print(show_commands())    

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
