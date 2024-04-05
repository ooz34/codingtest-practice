def solution(arr1, arr2):
    len_1row = len(arr1)
    len_lcol = len(arr1[0])
    len_2col = len(arr2[0])
    answer = [[0 for _ in range(len_2col)] for _ in range(len_1row)]
    
    for i in range(len_1row):
        for j in range(len_2col):
            for k in range(len_lcol):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer