'''Написать функцию fill_specializations, которая принимает список кортежей из специальности и имени и возвращает словарь,
где в качестве ключей специальности, а в качестве значений - списки имен. '''

from collections import defaultdict
from typing import List, Tuple


def fill_specializations(specializations: List[Tuple[str, str]]):
    default_dict = defaultdict(list)
    for spec, name in specializations:
        default_dict[spec].append(name)
    return dict(default_dict)

specs=[('Sales', 'John Doe'), ('Sales', 'Martin Smith'), ('Accounting', 'Jane Doe'), ('Marketing', 'Elizabeth Smith'), ('Marketing', 'Adam Doe')]
print(fill_specializations(specs))

