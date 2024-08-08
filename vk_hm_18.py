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

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
