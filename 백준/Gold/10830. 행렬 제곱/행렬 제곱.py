import sys
sys.setrecursionlimit(10**6)
n, b = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def multiply_matrix(mat1, mat2):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for z in range(n):
                res[i][j] += mat1[i][z] * mat2[z][j] % 1000
    return res
    
def power_matrix(mat, exp):
    if exp == 1:
        return mat
    else:
        temp = power_matrix(mat,exp//2)
        temp = multiply_matrix(temp, temp)
        if exp%2 == 0:
            return temp
        else:
            return multiply_matrix(temp, mat)
            
result = power_matrix(mat, b)
result = [[e % 1000 for e in row] for row in result]
for row in result:
    print(*row)