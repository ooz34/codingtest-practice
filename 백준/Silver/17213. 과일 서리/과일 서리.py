import math
n = int(input())
m = int(input())
print(math.comb((m-n)+(n-1), n-1))