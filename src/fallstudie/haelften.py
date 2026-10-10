import sys
halfs = int(input("anzahl hälften: "))
if halfs < 1:
    print("ungültig")
    sys.exit()
elif halfs == 1:
    print(" 1 Hälfte")
    sys.exit()

whole = halfs // 2
lefts = halfs%2

if lefts == 1:
    print(f"{halfs} Hälften: {whole} Ganze, eine Hälfte")
else: 
    print(f"{halfs} Hälften: {whole} Ganze, keine Hälfte")