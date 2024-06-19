import sys
n = int(sys.stdin.readline().rstrip())
counter = [0]*26
for _ in range(n):
    lname = sys.stdin.readline().rstrip()
    counter[ord(lname[0])-97] += 1
ans = ""
for i, n in enumerate(counter):
    if n >= 5:
        ans += chr(i+97)
print(ans if ans else 'PREDAJA')