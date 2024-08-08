span = input()
span = list(map(int, span.split()))
for val in map(lambda x: x**2 if x % 2 != 0 else -x, range(span[0], span[1], span[2])):
    print(val)
