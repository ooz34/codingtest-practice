import sys
while True:
    tri = list(map(int, sys.stdin.readline().split()))
    if max(tri) == 0:
        break
    tri.sort()
    if tri[0]**2 + tri[1]**2 == tri[2]**2:
        print('right')
    else:
        print('wrong')