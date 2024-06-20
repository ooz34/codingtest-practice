s, m = map(int, input().split())
coins = [512,256,128,64,32,16,8,4,2,1]

for val in coins:
    if s >= val:
        s -= val
    if s == 0:
        print('No thanks')
        exit(0)
        
for val in coins:
    if val <= m:
        m -= val
        if val <= s:
            s -= val
    if s == 0:
        print('Thanks')
        exit(0)

print('Impossible')