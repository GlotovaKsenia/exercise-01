l_r = [2,1,4,2,1,4]
j_r = [3,6,4,1,1,5]

round = 1
l_p = 0
j_p = 0

while (l_p < 3 and j_p < 3) and round <= len(l_r):
    print(f"Runde {round}: Lena {l_r[round-1]}, Jonas {j_r[round-1]}")
    
    if l_r[round-1] > j_r[round-1]:
        l_p += 1
    elif l_r[round-1] < j_r[round-1]:
        j_p += 1
    else:
        pass  # Bei Gleichstand passiert nichts
        
    print(f"Lena: {l_p}, Jonas: {j_p}\n")
    round += 1

# Gewinner-Ausgabe
if l_p > j_p:
    print("Lena hat gewonnen!")
elif j_p > l_p:
    print("Jonas hat gewonnen!")
else:
    print("Unentschieden nach allen Runden!")
