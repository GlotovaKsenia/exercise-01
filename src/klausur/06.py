def add(a: float, b: float)->float:
    result = a + b
    return round(result,2)

def total_amount(amounts: list)->float:
    total = 0
    for i in amounts:
        total = add(total, i)
    return total

amount=[1,2,3]
print(total_amount(amount))

def line_total(price: float, quantity: int = 1)-> float: #parameter price und quantity
    return round(price*quantity,2)

coffee = 2.0
print(line_total(coffee, 3))#6.0 argument coffee und 3
print(line_total(quantity = 4, price=0.9))#3.6 agrument 4 und 0.9 parameter quan und pr
print(line_total(1.2))#1.2 argument

def lowhigh(amounts: list[float])-> tuple[float,float]:
    low= amounts[0]
    high= amounts[0]
    for a in amounts:
        if a < low:
            low = a
        if a > high:
            high = a
    return low, high

low, high = lowhigh([412.5,380.0,512.75])
print(low,high)

discount = 0.1
def price(price: float)-> float:
    discount=0.05
    return round(price*(1-discount),2)

def raise_discount()-> None:
    global discount
    discount = 0.2

print(price(10)) #9.5
print(discount)#0.1
raise_discount()
print(discount)#0.2
print(price(10))#9.5

def add_item(cart: list[str], article: str) -> None:
    cart.append(article)


def add_one(count: int) -> None:
    global items
    items = count + 1


shopping_cart = ["Brezel"]
items = 1
add_item(shopping_cart, "Kaffee")
add_one(items)
print(shopping_cart)#[Brezel, Kaffee]
print(items)#1