'''
Python dataclasses
'''
from dataclasses import dataclass, field
import random
import string

# generate random id
def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))

@dataclass(kw_only=True)
class Person:
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory = list)
    id: str = field(init=False, default_factory = generate_id)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_string = f"{self.name}, {self.address}"

    def is_present(self, text: str) -> bool:
        return text in self._search_string

def main() -> None:
    person = Person(name='pramod', address='KL, Malaysia')
    print(person)
    text = input('Enter string to search ->')
    print(f'{text} is present in string: {person.is_present(text)}')

if __name__ == '__main__':
    main()

