from components import Field
import re

from utils import InvalidValue


class Phone(Field):
    def __init__(self, value):
        self.value = self.validate_number(value)
        super().__init__(value)

    @staticmethod
    def validate_number(value):
        if not re.fullmatch(r"\d{10}", value):
            raise InvalidValue(
                "Invalid number. It must contain only numbers and 10 digits."
            )
        return value