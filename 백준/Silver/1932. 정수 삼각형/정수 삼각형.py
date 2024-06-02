import sys
n = int(sys.stdin.readline().rstrip())
tri = []
for _ in range(n):
    tri.append(list(map(int, sys.stdin.readline().split())))

tri.reverse()
for i in range(n-1):
    for j in range(n-i-1):
        tri[i+1][j] += max(tri[i][j], tri[i][j+1])

print(tri[n-1][0])