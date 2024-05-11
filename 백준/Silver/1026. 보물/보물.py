import sys
n = int(sys.stdin.readline().strip())
a_list = sorted((map(int, sys.stdin.readline().split())))
b_list = sorted(map(int, sys.stdin.readline().split()), reverse=True)
s = 0
for a, b in zip(a_list, b_list):
    s += a*b
print(s)