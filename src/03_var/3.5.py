# betrag = int(input("Rückgeld in Cent: "))

# euro_2 = betrag//200
# rest = betrag%200
# print("2 Euro: ", euro_2, rest)

# euro_1 = rest//100
# rest = rest%100
# print("1 Euro: ", euro_1, rest)

# cent_50 = rest//50
# rest = rest%50
# print("50 cent: ", cent_50, rest)

# cent_20 = rest//20
# rest = rest%20
# print("20 cent: ", cent_20, rest)

# cent_10 = rest//10
# rest = rest%10
# print("10 cent: ", cent_10, rest)

# wechselgeld = [100,50,20,10,5,2,1,0.5,0.2,0.1]

# rest = float(input("Restgeld: "))

# for geld in wechselgeld:
#     anzahl = rest//geld
#     rest = rest%geld
#     print(geld,": ", anzahl)

# Alle Werte in Cent angeben (ganze Zahlen statt Floats)
wechselgeld_cent = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10]

# Eingabe in Euro einlesen und sofort in Cent umrechnen (mal 100)
# Wir runden zur Sicherheit, um Float-Ungenauigkeiten beim Multiplizieren abzufangen
rest_cent = round(float(input("Restgeld in Euro (z.B. 12.50): ")) * 100)

for geld_cent in wechselgeld_cent:
    anzahl = rest_cent // geld_cent
    rest_cent = rest_cent % geld_cent
    
    # Optional: Nur Münzen/Scheine anzeigen, die auch wirklich gebraucht werden
    if anzahl > 0:
        # Wieder zurück in Euro rechnen für die schöne Ausgabe
        geld_euro = geld_cent / 100
        print(f"{geld_euro:.2f} €: {anzahl}x")