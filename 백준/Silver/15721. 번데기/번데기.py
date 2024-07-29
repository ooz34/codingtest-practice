import sys
a = int(sys.stdin.readline().rstrip())
t = int(sys.stdin.readline().rstrip())
student = list(range(a))
s = sys.stdin.readline().rstrip()
bf = ['0101'+'0'*i+'1'*i for i in range(2, 101)]
tot = 0
scnt = 0
isEnd = False
for r in bf:
    for ch in r:
        tot += 1
        if ch == s:
            scnt += 1
            if scnt == t:
                isEnd = True
                break
    if isEnd: break
print(student[tot%a-1])