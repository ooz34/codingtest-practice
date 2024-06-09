import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, a, b = map(int, sys.stdin.readline().split())
    m = min(a, b)
    cnt = n
    while m % pow(2, cnt) != 0:
        cnt -= 1
    print(n-cnt)