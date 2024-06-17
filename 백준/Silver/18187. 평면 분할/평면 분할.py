n = int(input())
lines = [0, 0, 0]
cnt = 1
for i in range(n):
    cnt += 1 + sum(lines) - lines[i%3]
    lines[i%3] += 1
print(cnt)