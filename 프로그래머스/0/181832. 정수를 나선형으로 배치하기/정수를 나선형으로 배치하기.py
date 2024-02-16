def solution(n):
    answer = [[0]*n for x in range(n)]
    num = 1
    row = 0
    col = 0
    
    for i in range(n,0,-2):
        for j in range(i):
            answer[row][col] = num
            num += 1
            col += 1
        row += 1
        col -= 1
        
        for j in range(i-1):
            answer[row][col] = num
            num += 1
            row += 1
        row -= 1
        col -= 1
        
        for j in range(i-1):
            answer[row][col] = num
            num += 1
            col -= 1
        row -= 1
        col += 1

        for j in range(i-2):
            answer[row][col] = num
            num += 1
            row -= 1
        row += 1
        col += 1    
    
    return answer