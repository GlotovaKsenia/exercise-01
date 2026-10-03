# gross_price_interactive.py
# Vom Algorithmus zum Programm: lesen, rechnen, ausgeben.
name = input("Name des Artikels: ")
net_price = float(input("Nettopreis in Euro: "))
tax_rate = float(input("Steuersatz (z. B. 0.19): "))

gross_price = round(net_price * (1 + tax_rate), 2)
print("Artikel:", name)
print("Bruttopreis:", gross_price, "Euro")
