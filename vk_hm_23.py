

from typing import List

def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
    numsi = []
    index = []
    for i, el1 in enumerate(nums1):
        numsi.append(i)
    for i, el1, el2 in zip(numsi, nums1, nums2):
        if el1 < el2:
            index.append(i)
    return index
            

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
