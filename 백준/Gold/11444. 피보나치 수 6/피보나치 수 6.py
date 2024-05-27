n = int(input())
def fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fib(n//2)
        c = a*(2*b -a) % 1000000007  
        d = (a*a + b*b) % 1000000007  
        if n%2 == 0:
            return(c, d)
        else:
            return(d, (c+d) % 1000000007)
print(fib(n)[0])