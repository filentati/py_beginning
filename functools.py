import functools

#частично фиксируем параметры
def lt(a,b):
    return a<b

lt_fixed = functools.partial(lt, b = 0)
print(lt_fixed(-5))

#декоратор кэширования для функции
import time
@functools.lru_cache()  
def sum(n):
    s = 0
    for i in range(n):
        s+=n
    return s

start = time.time()
sum(100000000)
print(time.time()-start)

start = time.time()
sum(100000000)
print(time.time()-start)

#Декоратор доопределяющий магические методы 
@functools.total_ordering
class Counter:
    def __init__(self, count):
        self.count = count
    
    def __eq__(self, other):
        return self.count == other.count
    
    def __lt__(self, other):
        return self.count < other.count
    
print(Counter(2) >= Counter(3))
