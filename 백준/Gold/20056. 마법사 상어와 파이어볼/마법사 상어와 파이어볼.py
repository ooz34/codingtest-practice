import sys
n, m, k = map(int, sys.stdin.readline().split())
graph = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    graph[r-1][c-1].append([m,s,d])
direc = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

#명령
for _ in range(k):
    graph_v2 = [[[] for _ in range(n)] for _ in range(n)]
    #이동
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                while graph[i][j]:
                    m, s, d = graph[i][j].pop()
                    nx, ny = (i+direc[d][0]*s)%n, (j+direc[d][1]*s)%n
                    graph_v2[nx][ny].append([m,s,d])
    #합치기+나누기
    for i in range(n):
        for j in range(n):
            if len(graph_v2[i][j]) > 1:
                tm = 0
                ts = 0
                td = []
                while graph_v2[i][j]:
                    mi, si, di = graph_v2[i][j].pop()
                    tm += mi
                    ts += si
                    if di&1:
                        td.append(0)
                    else:
                        td.append(1)
                m = tm//5
                if not m:
                    # 소멸
                    pass
                else:
                    s = ts//len(td)
                    isDiff = True
                    if len(set(td)) == 1:
                        isDiff = False
                    for d in range(4):
                        graph[i][j].append([m,s,d*2+isDiff])
            elif len(graph_v2[i][j]) == 1:
                graph[i][j].append(graph_v2[i][j].pop())

ans = 0
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            while graph[i][j]:
                m, _, _ = graph[i][j].pop()
                ans += m
print(ans)