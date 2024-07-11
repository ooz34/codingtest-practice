import sys
n, m = map(int, sys.stdin.readline().split())
alist = list(map(int, sys.stdin.readline().split()))
blist = list(map(int, sys.stdin.readline().split()))

ans = []
i, j = 0, 0
while i<n and j<m:
    if alist[i] <= blist[j]:
        ans.append(alist[i])
        i += 1
    else:
        ans.append(blist[j])
        j += 1

while i<n:
    ans.append(alist[i])
    i += 1
while j<m:
    ans.append(blist[j])
    j += 1
    
print(*ans)