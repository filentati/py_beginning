'''Написать функцию fill_missing_values, которая принимает два списка int-ов и делает из них один список кортежей, 
где в качестве элементов кортежа элементы списков на одинаковых позициях.Если один из список закончился, то в нужно заполнить значение в кортеже единицей.'''

from itertools import zip_longest
from typing import List, Tuple


def fill_missing_values(values_list_1: List[int], values_list_2: List[int]) -> List[Tuple[int, int]]:
    new_list = []
    for el1, el2 in zip_longest(values_list_1, values_list_2, fillvalue=1):
        new_list.append((el1, el2))
    return new_list


print(fill_missing_values([1, 2, 3], [2, 3, 4, 5]))
