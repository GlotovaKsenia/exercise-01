product = input("Produkt: ")
price = float(input("Preis: "))
taxes = int(input("Steuersatz in Prozent: "))
quantity = int(input("Anzahl: "))

price_brut = price * (1 + taxes/100)
totalprice = round(price_brut * quantity, 1)
print(f"{quantity} x {product}: {totalprice} Euro")