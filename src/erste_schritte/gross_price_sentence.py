# gross_price_interactive.py
# Vom Algorithmus zum Programm: lesen, rechnen, ausgeben.
name = input("Name des Artikels: ")
net_price = float(input("Nettopreis in Euro: "))
tax_rate = float(input("Steuersatz in Prozent: "))

gross_price = round(net_price * (1 + tax_rate / 100), 2)
print(f"{name} kostet {gross_price} Euro brutto.")