article = input("Artikel: ")
price_netto = float(input("Preis: "))
taxes = int(input("Steuersatz in Prozent: "))

price_brutto = price_netto * (1 + taxes/100)

print(f"{article}\n Preis: {price_brutto}")
