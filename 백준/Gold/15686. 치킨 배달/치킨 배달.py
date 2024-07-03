import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
city = []
house = []
chick = []
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    city.append(row)
    for j, d in enumerate(row):
        if d == 1:
            house.append((i+1, j+1))
        elif d == 2:
            chick.append((i+1, j+1))

ans = n*2*len(house)
for comb in combinations(chick, m):
    city_d_chick = 0
    for r1, c1 in house:
        d_chick = n*2
        for r2, c2 in comb:
            d_chick = min(d_chick, abs(r1-r2) + abs(c1-c2))
        city_d_chick += d_chick
    ans = min(ans, city_d_chick)
print(ans)