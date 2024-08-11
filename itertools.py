import itertools

gen = range(10)

gen_islice = itertools.islice(gen, 2, 8, 2)

for el in gen_islice:
    print(el)


l1 = [1, 2, 3]
l2 = [4, 5, 6, 7, 8]

for el1, el2 in zip(l1, l2):
    print(el1, el2)
    
for el1, el2 in itertools.zip_longest(l1, l2):
    print(el1, el2)


for el in itertools.combinations(l2, 2):
    print(el)
