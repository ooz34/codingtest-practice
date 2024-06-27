import sys
def quad_tree(sr, sc, n):
    t = data[sr][sc]
    global ans
    for i in range(sr, sr+n):
        for j in range(sc, sc+n):
            if t != data[i][j]:
                ans.append('(')
                quad_tree(sr, sc, n//2)
                quad_tree(sr, sc+n//2, n//2)
                quad_tree(sr+n//2, sc, n//2)
                quad_tree(sr+n//2, sc+n//2, n//2)
                ans.append(')')
                return
    ans.append(t)

n = int(sys.stdin.readline().rstrip())
data = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
ans = []
quad_tree(0, 0, n)
print(''.join(ans))