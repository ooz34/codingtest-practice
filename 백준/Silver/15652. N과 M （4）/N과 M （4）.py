import sys

n, m = map(int, sys.stdin.readline().split())
arr = []

def backtrack(start):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(start, n + 1):
        arr.append(i)
        backtrack(i)
        arr.pop()

backtrack(1)