import sys
def sol(n):
    temp = '1'*len(n)
    while True:
        if int(temp)%int(n) == 0:
            print(len(temp))
            break
        temp += '1'

while True:
    n = sys.stdin.readline().rstrip()
    if n=='':
        break
    sol(n)