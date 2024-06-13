num = list(map(int, input().split()))
num.sort()
while num[0] + num[1] <= num[2]:
    num[2] -= 1
print(sum(num))
