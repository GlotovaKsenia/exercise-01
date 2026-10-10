import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

diskriminante = b**2 - 4*a*c

if diskriminante < 0:
    print("Keine reellen Lösungen (negative Wurzel).")
else:
    x1 = (-b + math.sqrt(diskriminante)) / (2*a)
    x2 = (-b - math.sqrt(diskriminante)) / (2*a)
    print(f"x1: {x1}\nx2: {x2}")