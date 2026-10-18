class Product:
    artikelnummer: int = 0
    name: str = "unbekannt"
    warengruppe: str = "standart"
    nettopreis: float = 0.0

    def __init__(self, artikelnummer, name, warengruppe, nettopreis):
        self.artikelnummer = artikelnummer
        self.name = name
        self.warengruppe = warengruppe.lower()
        self.nettopreis = float(nettopreis)

    def brutto_preis(self, menge):
        if self.warengruppe == "lebensmittel":
            steuersatz = 0.07
        else:
            steuersatz = 0.19
            
        gesamter_nettopreis = self.nettopreis * menge
        gesamter_bruttopreis = gesamter_nettopreis * (1 + steuersatz)
        
        return round(gesamter_bruttopreis, 2)

sortiment = [
    Product(1, "Brezel", "lebensmittel", 1.00),
    Product(2, "Cola", "standard", 1.50),
    Product(3, "Apfel", "lebensmittel", 0.60)
]

student = input("student? ja/nein: ").strip().lower() == "ja"
print("Eingabe beginnt. Leere Eingabe beendet\n")
total = 0
while True:
    eingabe_name = input("Artikel: ").strip()
    if eingabe_name == "":
        break
        
    gefundenes_produkt = None
    for artikel in sortiment:
        if artikel.name.lower() == eingabe_name.lower():
            gefundenes_produkt = artikel
            break # Produkt gefunden, Schleife abbrechen
            
    if gefundenes_produkt is None:
        print(f"Artikel '{eingabe_name}' wurde nicht im Sortiment gefunden.\n")
        continue # Springt zum Anfang der Schleife für die nächste Eingabe
        
    quantity = int(input("Menge: "))
    if quantity < 1:
        print("Ungültige Menge!\n")
        continue

    preis = gefundenes_produkt.brutto_preis(quantity)
    print(f"{gefundenes_produkt.name:<15}{quantity:>3}x{preis:>7.2f} €\n")
    total += preis
if student:
    total * 0.95
print(f"{'Summe:':<19}{total:>7.2f} €")