def solution(park, routes):
    answer = [0,0]
    w = len(park[0])
    h = len(park)
    direction = {'N':-1, 'S':1, 'W':-1, 'E':1}
    
    for y, row in enumerate(park):
        flag = False
        for x, col in enumerate(row):
            if col == 'S':
                answer = [y, x]
                flag = True
                break
        if flag:
            break
    
    for route in routes:
        op, n = route.split(' ')
        y = answer[0]
        x = answer[1]
        d = direction[op]
        if op == 'N' or op == 'S':
            y += d * int(n)
            if y < 0 or y >= h:
                continue
            for i in range(answer[0] ,y+d , d):
                if park[i][x] == 'X':
                    break
            else:
                answer[0] = y
        else:
            x += d * int(n)
            if x < 0 or x >= w:
                continue
            for i in range(answer[1] ,x+d , d):
                if park[y][i] == 'X':
                    break
            else:
                answer[1] = x
      
    return answer