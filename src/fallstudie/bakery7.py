from typing import Any

TAX_FOOD = 0.07
TAX_STANDARD = 0.19

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

items_ids = list(CATALOGUE.keys())

def stock_value_recursive(ids: list[int], catalogue: dict[int,dict[str,int]])->float:
    if not ids:
        return 0
    current_id = ids[0]
    article = catalogue[current_id]

    gross_price = article["net_price"]*(article["tax_rate"] + 1)
    item_value = gross_price * article["stock"]

    return item_value + stock_value_recursive(ids[1:], catalogue)

total_value = round(stock_value_recursive(items_ids, CATALOGUE), 2)
print(total_value)

min_stock = 50

def reorder_quantity(catalogue: dict[int,dict[str,int]])-> list[list[int]]:
    reorder: list[list[int]] = []

    for id in catalogue:
        article = catalogue[id]
        
        if article["stock"] <= 5:
            reorder.append([id, min_stock - article["stock"]])
        else:
            reorder.append([id, 0])
    return reorder

def reorder_quantity_recursive(ids: list[int], catalogue: dict[int,dict[str,int]])-> list[list[int]]:
    if not ids:
        return []
    current_id = ids[0]
    current_article = catalogue[current_id]
    reorder = 0
    if current_article["stock"] <=5:
        reorder = min_stock - current_article["stock"]
    current_entry = [current_id, reorder]
    return current_entry + reorder_quantity_recursive(ids[1:], catalogue)

    


test = reorder_quantity(CATALOGUE)
test2 = reorder_quantity_recursive(items_ids,CATALOGUE)
print(test)
print(test2)