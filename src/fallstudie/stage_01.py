class Artikel:
    def __init__(self, nr, name, netto, steuersatz, bestand):
        self.nr = int(nr)
        self.name = str(name)
        self.netto = float(netto)
        self.steuersatz = int(steuersatz)
        self.bestand = int(bestand)

    def brutto(self):
        price = self.netto * (1 + self.steuersatz/100)
        return(round(price,2))

sortiment = {}
sortiment[1001] = Artikel(1001, "Brezel", 0.84, 7, 40)

artikel = int(input("Artikelnummer: "))
price = sortiment[artikel].brutto()
print(price)

    