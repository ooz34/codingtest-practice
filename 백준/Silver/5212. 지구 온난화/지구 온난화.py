import sys
r, c = map(int, sys.stdin.readline().split())
map1 = []
map2 = []
for _ in range(r):
    row = sys.stdin.readline().rstrip()
    map1.append(list(row))
    map2.append(list(row))
minx, miny, maxx, maxy = r-1, c-1, 0, 0
for i, row in enumerate(map1):
    for j, col in enumerate(row):
        cnt = 0
        if col == 'X':
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                nx, ny = i+dx, j+dy
                if 0<= nx <r and 0<= ny <c:
                    if map1[nx][ny] == '.':
                        cnt += 1
                else:
                    cnt += 1
            if cnt >= 3:
                map2[i][j] = '.'
            else:
                minx = min(minx, i)
                miny = min(miny, j)
                maxx = max(maxx, i)
                maxy = max(maxy, j)
for i in range(minx, maxx+1):
    for j in range(miny, maxy+1):
        print(map2[i][j], end='')
    print()