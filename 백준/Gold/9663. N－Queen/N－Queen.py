n = int(input())
cnt = 0
isused1 = [False for _ in range(n)]
isused2 = [False for _ in range(2*n)]
isused3 = [False for _ in range(2*n)]

def backtrack(row):
    global cnt
    if row == n: 
        cnt += 1
        return 
    for i in range(n): 
        if isused1[i] or isused2[i + row] or isused3[row - i + n - 1]: 
            continue
        isused1[i] = True
        isused2[i + row] = True
        isused3[row - i + n - 1] = True
        backtrack(row + 1)
        isused1[i] = False
        isused2[i + row] = False
        isused3[row - i + n - 1] = False

backtrack(0)
print(cnt)