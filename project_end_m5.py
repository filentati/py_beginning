'''Написать функцию rotate_list, которая принимает список целых чисел и целое число, которое будет задавать, сколько крутить список. 
Под кручением списка подразумевается забор элемента из конца списка и вставка его в начало списка. '''

from collections import deque
from typing import List


def rotate_list(nums: List[int], n: int):
    deq = deque(nums)
    for i in range(n):
        a = deq.pop()
        deq.appendleft(a)
    return list(deq)
        
    

print(rotate_list([1,2,3,4], 1))
