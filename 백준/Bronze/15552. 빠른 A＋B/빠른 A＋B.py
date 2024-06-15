import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    print(sum(list(map(int, sys.stdin.readline().split()))))