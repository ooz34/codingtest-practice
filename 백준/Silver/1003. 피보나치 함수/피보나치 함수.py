import sys
t = int(sys.stdin.readline().strip())
def cnt0(n):
    a, b = 1, 0
    for _ in range(n):
      a, b = b, a+b
    return a
def cnt1(n):
    a, b = 0, 1
    for _ in range(n):
      a, b = b, a+b
    return a

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    print(cnt0(n), end=' ')
    print(cnt1(n))