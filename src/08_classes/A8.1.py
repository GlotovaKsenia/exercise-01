from dataclasses import dataclass

@dataclass
class Article:
    number: int
    name: str
    net_price: float
    tax_rate: float
    stock: int

    @property
    def gross_price(self):
        return round(self.net_price * (1 + self.tax_rate), 2)

    @classmethod
    def from_csv_row(cls, row) -> Article:
        return cls(
            number=int(row["number"]),
            name=row["name"],
            net_price=float(row["net_price"]),
            tax_rate=float(row["tax_rate"]),
            stock=int(row["stock"])
        )

row: dict[str, str] = {
    "number": "2001",
    "name": "Kaffee",
    "net_price": "1.68",
    "tax_rate": "0.19",
    "stock": "100",
}

pretzel = Article(1001, "Brezel", 0.84, 0.07, 40)
print(pretzel.gross_price)

coffee = Article.from_csv_row(row)
print(coffee)