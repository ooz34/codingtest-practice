import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int,sys.stdin.readline().split()))

itv = []
for _ in range(M):
  itv.append(list(map(int, sys.stdin.readline().split())))  
  
prefix_sum = [0 for _ in range(N+1)]

for i, n in enumerate(num, start=1):
  prefix_sum[i] = prefix_sum[i-1] + n

for i, j in itv:
    part_sum = prefix_sum[j] - prefix_sum[i-1]
    print(part_sum)