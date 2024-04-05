import sys
y = int(sys.stdin.readline())

if y % 400 == 0:
    print(1)
    exit()
if y % 4 == 0 and y % 100 != 0:
    print(1)
    exit()
print(0)