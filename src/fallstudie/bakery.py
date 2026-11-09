from typing import Any

TAX_FOOD: float = 0.07
TAX_STANDARD: float = 0.19

CATALOGUE: dict[int, dict[str, Any]] = {
    1001: {
        "name": "Brezel",
        "group": "Backwaren",
        "subgroup": "Laugengebäck",
        "net_price": 0.84,
        "tax_rate": TAX_FOOD,
        "stock": 40,
    },
    1002: {
        "name": "Semmel",
        "group": "Backwaren",
        "subgroup": "Brötchen",
        "net_price": 0.47,
        "tax_rate": TAX_FOOD,
        "stock": 25,
    },
    2001: {
        "name": "Kaffee",
        "group": "Getränke",
        "subgroup": "Heißgetränke",
        "net_price": 1.68,
        "tax_rate": TAX_STANDARD,
        "stock": 100,
    },
    2002: {
        "name": "Wasser 0,5 l",
        "group": "Getränke",
        "subgroup": "Kaltgetränke",
        "net_price": 1.01,
        "tax_rate": TAX_STANDARD,
        "stock": 30,
    },
    3001: {
        "name": "Thermobecher",
        "group": "Zubehör",
        "subgroup": None,
        "net_price": 2.52,
        "tax_rate": TAX_STANDARD,
        "stock": 12,
    },
    3002: {
        "name": "Stofftasche",
        "group": "Zubehör",
        "subgroup": None,
        "net_price": 0.84,
        "tax_rate": TAX_STANDARD,
        "stock": 4,
    },
}

GROUPS: dict[str, Any] = {
    "name": "Bäckerei Berger",
    "articles": [],
    "subgroups": [
        {
            "name": "Backwaren",
            "articles": [],
            "subgroups": [
                {"name": "Laugengebäck", "articles": [1001], "subgroups": []},
                {"name": "Brötchen", "articles": [1002], "subgroups": []},
            ],
        },
        {
            "name": "Getränke",
            "articles": [],
            "subgroups": [
                {"name": "Heißgetränke", "articles": [2001], "subgroups": []},
                {"name": "Kaltgetränke", "articles": [2002], "subgroups": []},
            ],
        },
        {"name": "Zubehör", "articles": [3001, 3002], "subgroups": []},
    ],
}

def gross_price(net: float, tax_rate: float):
    return round(net*(1+tax_rate), 2)

def stock_value(group: dict[str, Any]):
    own = sum(
        gross_price(CATALOGUE[number]["net_price"], CATALOGUE[number]["tax_rate"]) * CATALOGUE[number]["stock"]
        for number in group["articles"]
    )
    nested_group = sum(stock_value(subgroups) for subgroups in group["subgroups"])
    return round(own + nested_group, 2)

MIN_STOCK: int = 5
REORDER_TARGET: int= 20

def reorder(number: int):
    stock: int = CATALOGUE[number]["stock"]
    if stock >= MIN_STOCK:
        return 0
    return REORDER_TARGET - stock

if __name__=="__main__":
    print("Overall bakery stock: ", stock_value(GROUPS), "Euro")

    for number, article in CATALOGUE.items():
        quantity = reorder(number)
        if quantity > 0:
            print(f"low stock level. Reorder {article["name"]} {quantity} x")

    answer = input("Article number: ")
    try:
        number = int(answer)
        article = CATALOGUE[number]
    except ValueError:
        print("enter a number as article number")
    except KeyError:
        print("unknown article number")
    else:
        gross = gross_price(article["net_price"], article["tax_rate"])
        print(article["name"], ":", gross, "€, in stock: ", article["stock"])