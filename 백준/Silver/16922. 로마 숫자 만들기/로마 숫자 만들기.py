from itertools import combinations_with_replacement
n = int(input())
num = [1, 5, 10, 50]
res = set()
for c in combinations_with_replacement(num, n):
    res.add(sum(c))
print(len(res))