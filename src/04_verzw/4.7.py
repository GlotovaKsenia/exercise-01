import sys
import math
a = float(input("a: "))
if a == 0:
    print("ungültig")
    sys.exit()

b = float(input("b: "))
c = float(input("c: "))

d = b**2 - 4*a*c

if d > 0:
    results = 2
elif d == 0:
    results = 1
else:
    results = 0

if results == 0:
    print("keine Lösungen")
    sys.exit()
elif results == 1:
    x = -b/(2*a)
    if x < 0:
        print("Lösung negativ")
    print("Lösung ist: x = ", x)    
else:
    x1 = (- b + math.sqrt(d))/(2*a)
    x2 = (- b - math.sqrt(d))/(2*a)
    if x1 < 0 or x2 < 0:
        print("Mind. 1 Lösung negativ")
    print("Lösungen: x1 = ", x1, "x2 = ", x2)

