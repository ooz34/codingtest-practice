import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
even_first = 0
odd_first = 0
e_idx = -1
o_idx = -1
for i, num in enumerate(a):
    if num & 1:
        o_idx += 1
        odd_first += i - o_idx
    else:
        e_idx += 1
        even_first += i - e_idx
print(min(even_first, odd_first))