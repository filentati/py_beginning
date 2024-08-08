'''Необходимо написать генераторную функцию solution, которая будет фильтровать данные из последовательности data функцией func_filter,
к полученным данным применять функцию func_map и возвращать в качестве значения каждый второй элемент полученной последовательности'''

def cache_deco(func):
    cache = {}
    def wrapper(*args, **kwargs):
        if (args, tuple(kwargs.items())) in cache:
            return cache[(args, tuple(kwargs.items()))]
        else:
            result = func(*args, *kwargs)
            cache[(args, tuple(kwargs.items()))] = result
            return result
    return wrapper

def solution(func_map, func_filter, data):
    i = 0
    for item in data:
        if func_filter(item):
            mapped_item = func_map(item)
            if i % 2 == 0:
                yield mapped_item
            i += 1

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
