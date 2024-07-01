from functools import reduce
n = int(input())
if not n:
    print(1)
else:
    arr = list(range(1, n+1))
    print(reduce(lambda x, y: x*y, arr))