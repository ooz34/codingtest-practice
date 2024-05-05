from collections import deque
a, b = map(int, input().split())
q = deque()
q.append((a, 1))

while q:
    curr, cnt = q.popleft()
    if curr > b:
        continue
    if curr == b:
        print(cnt)
        break
    q.append((curr*2, cnt+1))
    q.append((int(str(curr)+'1'), cnt+1))
else:
    print(-1)