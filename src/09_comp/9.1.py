#Bei der Komposition erstellt das Ganze das 
# Teil selbst im eigenen Code (es gehört ihm exklusiv 
# und wird mit ihm vernichtet), während bei der 
# Aggregation ein bereits eigenständig existierendes 
# Teil von außen als Parameter hineingereicht wird 
# (es überlebt das Ganze).

# order.py
# Eine Bestellung setzt sich aus Positionen zusammen; jede Position
# verweist auf einen Artikel.


class Article:
    def __init__(self, number: int, name: str, net_price: float, tax_rate: float) -> None:
        self.number = number
        self.name = name
        self.net_price = net_price
        self.tax_rate = tax_rate

    def gross_price(self) -> float:
        return round(self.net_price * (1 + self.tax_rate), 2)


class OrderLine:
    """Eine Bestellposition. Aggregation: sie verweist nur auf den Artikel,
    der Artikel existiert auch ohne diese Position (er steht im Sortiment)."""

    def __init__(self, article: Article, quantity: int) -> None:
        self.article = article
        self.quantity = quantity

    def line_total(self) -> float:
        return round(self.article.gross_price() * self.quantity, 2)


class Order:
    """Eine Bestellung. Komposition: ihre Positionen gehören ihr allein,
    ohne die Bestellung gibt es diese Positionen nicht."""

    def __init__(self) -> None:
        self.lines: list[OrderLine] = []

    def add(self, article: Article, quantity: int) -> OrderLine:
        line = OrderLine(article, quantity)
        self.lines.append(line)
        return line

    def total(self) -> float:
        return round(sum(line.line_total() for line in self.lines), 2)


#if __name__ == "__main__":
    # nur beim direkten Ausführen, nicht wenn ein anderes Skript
    # (z. B. orders_list.py) diese Klassen importiert
pretzel = Article(1001, "Brezel", 0.84, 0.07)
coffee = Article(2001, "Kaffee", 1.68, 0.19)

order = Order()
order.add(pretzel, 2)
order.add(coffee, 1)
print(order.total())
# 3.8

# customers.py
# Vererbung: Student und RegularCustomer erben von Customer und überschreiben
# discount_rate(). Derselbe Aufruf, drei verschiedene Ergebnisse: Polymorphie.


class Customer:
    def __init__(self, name: str) -> None:
        self.name = name

    def discount_rate(self) -> float:
        return 0.0


class Student(Customer):
    def __init__(self, name: str, student_id: int) -> None:
        super().__init__(name)  # ruft Customer.__init__ auf, setzt self.name
        self.student_id = student_id

    def discount_rate(self) -> float:
        return 0.10


class RegularCustomer(Customer):
    def __init__(self, name: str, since_year: int) -> None:
        super().__init__(name)
        self.since_year = since_year

    def discount_rate(self) -> float:
        return 0.15
    
class Employee(Customer):
    def __init__(self, name, staff_no):
        super().__init__(name)
        self.staff_no = staff_no

    def discount_rate(self):
        return 0.2



customers: list[Customer] = [
    Customer("Alex"),
    Student("Lena", 723456),
    RegularCustomer("Jonas", 2023),
    Employee("Mika",17)
]

for customer in customers:
    print(customer.name, customer.discount_rate())
# Alex 0.0
# Lena 0.1
# Jonas 0.15

print(isinstance(customers[1], Customer))
print(isinstance(customers[0], Student))
print(isinstance(customers[3], Employee))
