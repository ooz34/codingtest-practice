import sys
q = int(sys.stdin.readline().rstrip())
for _ in range(q):
    a = int(sys.stdin.readline().rstrip())
    print(1 if (a&(-a)) == a else 0)