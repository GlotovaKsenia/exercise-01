from checkout import line_total
class Article:
    def __init__(self, number, name, net_price, tax_rate, stock):
        self.no = number
        self.n = name
        self.np = net_price
        self.p = tax_rate
        self._stock = stock

    def sell(self, quantity):
        self._stock -= quantity
        if self._stock <0:
            raise ValueError("Bestand reicht nicht")
        elif self._stock <= 5:
            print("jetzt unterm Mindestbestand")
            return False
        else:
            print("Menge wurd abgezogen")
  
        return True

    def gross_price(self):
        return round(self.np * (1 + self.p), 2)

    def stock_on_hand(self):
        return self._stock

class OrderLine:
    def __init__(self, article: Article, amount):
        self.article = article
        self.a = amount
        self.unit_price = article.gross_price()

    def amount(self):
        return line_total(self.unit_price, self.a)

class Order:
    def __init__(self, cust, student: bool = False):
        self.cust = cust
        self.s = student
        self.lines: list[OrderLine] = []
        self.warnings: list[str] = []

    def add(self, article, quantity):
        low_stock = article.sell(quantity)
        line = OrderLine(article, quantity)
        self.lines.append(line)
        if low_stock == False:
            self.warnings.append(f"Achtung: {article.n} nur noch {article.stock_on_hand()} Stück")
        return line

    def subtotal(self):
        return round(sum(line.amount() for line in self.lines),2)

    def total(self):
        subtotal = self.subtotal()
        if self.s:
            return subtotal * 0.995
        return subtotal
    def daily_total(orders: list[Order]):
        return round(sum(order.total() for order in orders), 2)

if __name__ == "__main__":
    # 1. Artikel anlegen (Preis 2.50 netto, 19% MwSt = 2.975 -> gerundet 2.98 brutto)
    coffee = Article(number=1, name="Kaffee", net_price=2.50, tax_rate=0.19, stock=10)
    
    print(f"Bruttopreis Kaffee: {coffee.gross_price()} €")
    
    # 2. Bestellung anlegen
    order = Order(cust="Max Mustermann", student=False)
    
    # 3. Artikel hinzufügen (Menge 3 -> neuer Bestand 7)
    order.add(coffee, 3)
    
    print(f"Zwischensumme: {order.subtotal()} €")
    print(f"Aktueller Bestand: {coffee.stock_on_hand()}")
    
    # 4. Test mit niedrigem Bestand (Menge 4 -> Bestand wird 3, <= 5 -> Warnung)
    order.add(coffee, 4)
    print("Warnungen in Bestellung:", order.warnings)