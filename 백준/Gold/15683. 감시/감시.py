import sys

n, m = map(int, sys.stdin.readline().split())
office = []
cctv = []
xy = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 북서남동
cctv_type = {
    1:[[0],[1],[2],[3]],
    2:[[0,2], [1,3]],
    3:[[0,1],[1,2],[2,3],[3,0]],
    4:[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    5:[[0,1,2,3]]
}

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    office.append(row)
    for j, num in enumerate(row):
        if num in range(1, 6):
            cctv.append([num, i, j])

def update_watched_area(office, cx, cy, angle):
    for direc in angle:
        nx, ny = cx, cy
        while True:
            nx += xy[direc][0]
            ny += xy[direc][1]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if office[nx][ny] == 6:
                break
            elif not office[nx][ny]:
                office[nx][ny] = -1

def backtrack(depth, office):
    global blind_spot
    
    if depth == len(cctv):
        cnt = 0
        for row in office:
            cnt += row.count(0)
        blind_spot = min(blind_spot, cnt)
        return
    
    type, cx, cy = cctv[depth]
    for angle in cctv_type[type]:
        temp_office = [row[:] for row in office]
        update_watched_area(temp_office, cx, cy, angle)
        backtrack(depth+1, temp_office)
        
blind_spot = 64
backtrack(0, office)
print(blind_spot)