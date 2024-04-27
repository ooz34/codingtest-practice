import sys

n, m = map(int, sys.stdin.readline().split())
nlist = sorted(list(map(int, sys.stdin.readline().split())))
arr = []

def backtrack(start):
    if len(arr) == m:
        print(*arr)
        return
    curr = 0
    for i in range(start, n):
        if curr != nlist[i]:
            arr.append(nlist[i])
            curr = nlist[i]
            backtrack(i)
            arr.pop()

backtrack(0)