s = input()
k = input()
s2 = ''
for ch in s:
    if ch not in ['0','1','2','3','4','5','6','7','8','9']:
        s2 += ch
print(1 if k in s2 else 0)