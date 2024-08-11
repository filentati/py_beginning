import collections 

l = [1, 1, 1, 2, 2, 3, 4]

counter = collections.Counter(l)
print(counter.most_common(1))

#Двустороный список 
deq = collections.deque(l)
deq.append(5)
deq.appendleft(0)
print(deq)

#Словарь с неявной обработкой 
default_dict_list = collections.defaultdict(list)
default_dict_list[1].append(0)
default_dict_list[2].append('abc')
print(default_dict_list)

#цепной словарь 
d1 = {1: 111, 2: 222, 3:333}
d2 = {3: 1, 4: 444}
chin_map = collections.ChainMap(d1, d2)
print(chin_map[3])
