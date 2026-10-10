# dungeon.py
# Data Dungeon, Stufe 1: Spielstart mit Begrüßung und Startwerten.
from greet import greet
name = input("Wie heißt du? ")

energy = 100
experience = 0
crystals = 0

greet(name, energy, experience, crystals)

messwerte = [12,15,11,14,48]
print("Messwerte im ersten Raum: ", end=" ")
for i in messwerte:
    wert = i
    print(wert, end=" ")

print(messwerte)
print("mittelwert:", sum(messwerte)/len(messwerte))