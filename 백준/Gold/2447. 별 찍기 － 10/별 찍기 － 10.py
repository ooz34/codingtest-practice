n = int(input())

def pattern(n):
    if n==1:
        return '*'
    blocks = pattern(n//3)
    result = []
    
    for block in blocks:
        result.append(block * 3)
    for block in blocks:
        result.append(block + ' '*(n//3) + block)
    for block in blocks:
        result.append(block * 3)
        
    return result

result = pattern(n)
for row in result:
    print(row)