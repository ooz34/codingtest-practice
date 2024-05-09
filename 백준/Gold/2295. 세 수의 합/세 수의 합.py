import sys
from itertools import combinations_with_replacement
n = int(sys.stdin.readline().strip())
u = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])

sums = set()
for c in combinations_with_replacement(u, 2):
    sums.add(sum(c))

answer = 0
for i, num  in reversed(list(enumerate((u)))):
    for j in range(i+1):
        if num-u[j] in sums:    
            answer = max(num, answer)
        
print(answer)