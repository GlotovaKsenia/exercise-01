def gcd(a: int, b: int) -> int:
    while b!= 0:
        a, b = b, a % b
    return a

print(gcd(75, 45))
#75 45
#45 30
#30 15
#15 15
