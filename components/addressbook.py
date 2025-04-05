from collections import UserDict
from datetime import datetime, timedelta

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return "Record deleted."
        return KeyError()

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.today().date()

        for record in self.data.values():
            if record.birthday:
                birthday = record.birthday.value 
                birthday_this_year = birthday.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                if (
                    today <= birthday_this_year <= today + timedelta(days=7)
                ): 
                    if birthday_this_year.weekday() == 5:  
                        birthday_this_year += timedelta(days=2)
                    elif birthday_this_year.weekday() == 6:
                        birthday_this_year += timedelta(days=1)

                    upcoming_birthdays.append(
                        {
                            "name": record.name.value,
                            "congratulation_date": birthday_this_year.strftime("%d.%m.%Y"),
                        }
                    )

        return upcoming_birthdays if upcoming_birthdays else "No upcoming birthdays."

