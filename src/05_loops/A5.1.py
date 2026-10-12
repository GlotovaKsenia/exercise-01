lines = [("Brezel", 12, 0.90),
         ("Kaffee", 3, 2.00),
         ("Wasser 0.5 l", 5, 1.20)]

titel = [("Artikel", "Menge", "Preis", "Betrag")]

for name, quantity, gross, amount in titel:
    print(f"{name:<15}{quantity:>6}{gross:>8}{amount:>9}")

print("-"*(15+6+8+9))
result=0
for name, quantity, gross in lines:
    amount = round(quantity*gross,2)
    result += amount
    print(f"{name:<15}{quantity:>6}{gross:>8}{amount:>9.2f}")
print("-"*(15+6+8+9))

print(f"{'Summe':<15}{' '*(6+8)}{result:>9.2f}")