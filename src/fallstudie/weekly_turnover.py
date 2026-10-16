wochentage = ["mo","di","mi","do","fr"]
umsatz = [412.5,388.2,501.1,275.4,460]
x=0
i=0
s=0
for u in umsatz:
    if u > x:
        x = u
        best = i
    i += 1
    s+=u

a = s/i
print(f"summe: {s:.2f}")
print(f"durchschnitt: {a:.2f}")
print(f"bester tag: {wochentage[best]} {x:.2f}")