from rebotics_sdk.rcdb.fields import BaseField
from rebotics_sdk.rcdb.entries import BaseEntry


class EntryTypeBuilder:
    def __init__(self):
        self.fields = {}

    def add_field(self, name, field: BaseField):
        if name in self.fields:
            raise ValueError(f'Field with name {name} already exists.')

        if not isinstance(field, BaseField):
            # when you don't set proper BaseField subclassed object, the field will not be registered
            # meaning that it will not function properly
            raise ValueError(f'Field {name} is not an instance of BaseField.')

        self.fields[name] = field

    def build(self):
        return type('Entry', (BaseEntry,), self.fields)
