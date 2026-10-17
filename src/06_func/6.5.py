def factorial(n: int) -> int:
    if n == 0:
        return 1

    x = 1
    for i in range(1,n+1):
        x = x*i
    return x

print(factorial(5))

def fac(n: int) -> int:
    if n == 0:
        return 1
    x = n
    while n > 1:
        x *= (n-1)
        n -= 1
    return x

print(fac(5))