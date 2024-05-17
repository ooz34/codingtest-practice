from collections import deque
n, w, l = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bridge = deque()

time = 0
while True:
    time += 1
    if bridge and time - bridge[0][1] >= w:
        l += bridge[0][0]
        bridge.popleft()
    if trucks and trucks[0] <= l:
        l -= trucks[0]
        bridge.append((trucks[0], time))
        trucks.popleft()
    if not trucks and not bridge:
        break
print(time)