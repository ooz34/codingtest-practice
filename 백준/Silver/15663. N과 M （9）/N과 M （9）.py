import sys

n, m = map(int, sys.stdin.readline().split())
nlist = sorted(list(map(int, sys.stdin.readline().split())))
arr = []
visited = [False for _ in range(n)]

def backtrack():
    if len(arr) == m:
        print(*arr)
        return
    curr = 0
    for i in range(n):
        if not visited[i] and curr != nlist[i]:
            arr.append(nlist[i])
            visited[i] = True
            curr = nlist[i]
            backtrack()
            arr.pop()
            visited[i] = False

backtrack()