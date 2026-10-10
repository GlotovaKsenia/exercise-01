k0 = float(input("Startkapital: "))
p = float(input("Prozentsatz in Prozent: "))
n = float(input("Vergangene Jahre: "))

r = k0 * (1 + p/100) * n
print("Deine Werte:", k0, p, n)
print(f"Endkapital: {r:.2f}")