import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
balloons = deque(list(enumerate(map(int, sys.stdin.readline().split()))))

ans = []
while balloons:
    idx, num = balloons.popleft()
    ans.append(idx+1)
    if num > 0:
        balloons.rotate(-(num-1))
    else:
        balloons.rotate(-num)
print(*ans)