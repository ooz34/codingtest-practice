a = int(input())
b = input().rstrip()
for ch in b[::-1]:
    print(a*int(ch))
print(a*int(b))