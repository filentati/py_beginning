def repeat_deco(n=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n - 1):  # Выполняем n-1 раз
                func(*args, **kwargs)
            return func(*args, **kwargs)  # Возвращаем результат последнего вызова
        return wrapper
    return decorator

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
