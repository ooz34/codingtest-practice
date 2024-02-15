def solution(arr):
    answer = 0
    
    while True:
        answer += 1        
        flag = False

        for i, n in enumerate(arr):
            if n >= 50:
                if n % 2 == 0:
                    arr[i] = n // 2
                    flag = True
                    continue
            if n < 50:
                if n % 2 == 1:
                    flag = True
                    arr[i] = n * 2 + 1

        if not flag:
            return answer-1