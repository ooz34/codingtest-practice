import sys
t = int(sys.stdin.readline().strip())
tests = []
for _ in range(t):
    tests.append(sys.stdin.readline().split())

for r, s in tests:
    temp = ''
    for p in s:
        temp += p*int(r)
    print(temp)