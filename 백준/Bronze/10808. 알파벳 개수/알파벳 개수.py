cnt = [0]*26
for ch in input():
    cnt[ord(ch)-97] += 1
print(*cnt)