import sys
n = int(sys.stdin.readline().strip())
max_weight = sorted([int(sys.stdin.readline().strip()) for _ in range(n)], reverse=True)

answer = 0
for i, mw in enumerate(max_weight):
    answer = max(answer, (i+1)*mw)
print(answer)