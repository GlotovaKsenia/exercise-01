discount_threshold = 10
discount_p = 0.05
def gross(net: float, p: float = 0.19)-> float:
    x = net * (p+1)
    return round(x, 2)

def line_total(price: float, n: int)-> float:
    total = round(price*n,2)
    if n >= discount_threshold:
        total = discount(total, discount_p)
    return total

def discount(total: float, p: float = 0.05) -> float:
    total = total *(1-p)
    return round(total,2)

def receipt_line(name:str, n: int, amount: float)-> str:
    return f"{name:<15}{n:>3} Stk {amount:>7.2f} €"
