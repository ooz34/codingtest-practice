import sys

A, B, C = map(int, sys.stdin.readline().split())
    
def sol(A, B, C):
    if B == 1:
        return A % C
    temp = sol(A, B//2, C)
    if B % 2 == 0:
        return temp * temp % C
    return (temp * temp % C) * A % C

print(sol(A, B, C))