import timeit

thousend = [1, 2, 3, 4, 5] * 200


# 1. Wir verpacken die Schleife in eine normale Funktion
def teste_schleife():
  total = 0.0
  for amount in thousend:
    total += amount


# 2. Wir verpacken sum() in eine normale Funktion
def teste_sum():
  total = sum(thousend)


# timeit misst jetzt direkt die Funktionen (völlig ohne Strings!)
time_loop = timeit.timeit(teste_schleife, number=1000)
time_sum = timeit.timeit(teste_sum, number=1000)

# 3. Ergebnisse ausgeben
print(f"Dauer for-Schleife: {time_loop:.6f} Sekunden")
print(f"Dauer sum()-Funktion: {time_sum:.6f} Sekunden")

# 4. Vergleich
if time_sum < time_loop:
  print("Die eingebaute sum()-Funktion war schneller.")
else:
  print("Die for-Schleife war schneller.")