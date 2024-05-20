import sys
n = int(sys.stdin.readline().strip())
plist = sorted(map(int, sys.stdin.readline().split()))
answer = 0
for i, p in enumerate(plist):
    answer += (n-i)*p
print(answer)
