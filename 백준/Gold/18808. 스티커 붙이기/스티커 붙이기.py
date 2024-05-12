import sys
n, m, k = map(int, sys.stdin.readline().split())
laptop = [[0]*m for _ in range(n)]

def rotate_90(sticker):
    sticker.reverse()
    return [list(row) for row in zip(*sticker)]

def can_attach(laptop, sticker, i, j):
    for k in range(len(sticker)):
        for l in range(len(sticker[0])):
            if sticker[k][l] == 1:
                if i + k >= n or j + l >= m or laptop[k+i][l+j] == 1:
                    return False
    return True

def attach(laptop, sticker, i, j):
    for k in range(len(sticker)):
        for l in range(len(sticker[0])):
            if sticker[k][l] == 1:
                laptop[k+i][l+j] = 1

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
    
    attached = False
    for _ in range(4):
        if attached:
            break
        for i in range(n):
            if attached:
                break
            for j in range(m):
                if can_attach(laptop, sticker, i, j):
                    attach(laptop, sticker, i, j)
                    attached = True
                    break
        else:
            sticker = rotate_90(sticker)
                
print(sum(sum(row) for row in laptop))