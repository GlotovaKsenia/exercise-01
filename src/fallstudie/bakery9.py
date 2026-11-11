from checkout import line_total
class InsufficientStockError(Exception):
    def __init__(self, article_name, requested, available):
        self.n = article_name
        self.r = requested
        self.a = available
        super().__init__(f"{self.n}: bestellt {self.r} Stück, verfügbar {self.a}")

class Customer:
    discount = 0
    
    def __init__(self, name):
        pass
        
    def discount_rate(self):
        return self.discount

class Student(Customer):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.s_id = student_id
        self.discount = 0.1
        
    def discount_rate(self):
        return self.discount

class RegularCust(Customer):
    def __init__(self, name, since_year):
        super().__init__(name)
        self.sy = since_year
        self.discount = 0.15 

    def discount_rate(self):
        return self.discount


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
            raise InsufficientStockError(self.n, quantity, self._stock+quantity)
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
    def __init__(self, customer: Customer):
        self.c = customer
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
        discount = self.c.discount_rate()
        subtotal = subtotal * (1- discount)
        return subtotal
    
    def daily_total(orders: list[Order]):
        return round(sum(order.total() for order in orders), 2)

if __name__ == "__main__":
    t = Student("Lena", 123)
    b = Article(1001, "brezel", 0.84, 0.07, 5)
    c = Article(1111, "Kaffee", 1.68, 0.19, 20000)
    order = Order(t)
    order.add(b, 6)
    order.add(c, 2)
    print(order.total())