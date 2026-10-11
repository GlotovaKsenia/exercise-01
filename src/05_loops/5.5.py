menu = ["1 Kassenbon starten", "2 Bestand prüfen", "3 Tagesbericht", "4 Beenden"]

for i in menu:
    print(i)

selected = [
    "Start",
    "Bestand: 40 Bezeln, 25 Semmeln, 100 Kaffee.",
    "Heutiger Tag",
    "Tschüss",
    "ungültig",
]

while True:
    auswahl = int(input("\nWählen (1-4): "))

    # Menüpunkt 1 bis 3 (im Code Index 0, 1, 2)
    if auswahl >= 1 and auswahl <= 3:
        print(selected[auswahl - 1])

    # Menüpunkt 4 zum Beenden (im Code Index 3)
    elif auswahl == 4:
        print(selected[3])  # "Tschüss"
        break  # Beendet die while-Schleife

    # Alles andere ist ungültig
    else:
        print(selected[4])  # "ungültig"