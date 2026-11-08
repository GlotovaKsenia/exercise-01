# article_v3_methods.py
class Article:
    def __init__(self, name: str, net_price: float, tax_rate: float) -> None:
        self.name = name
        self.net_price = net_price
        self.tax_rate = tax_rate

    def gross_price(self) -> float:
        return round(self.net_price * (1 + self.tax_rate), 2)

    def line_total(self, quantity) -> float:
        total = Article.gross_price(self)* quantity
        return round(total, 2)


pretzel = Article("Brezel", 0.84, 0.07)
print(pretzel.gross_price())
# 0.9
print(pretzel.line_total(12))