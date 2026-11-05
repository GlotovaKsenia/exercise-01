from typing import Any
bonus: int = 5000
p_bonus: float=0.005

def effective(k0, p) -> float:
    if k0 >= bonus:
        return round(p + p_bonus, 4)
    return p

def future(k0, p, y) -> float:
    return round(k0 * (1+p) ** y, 2)

def table(k0, p, y) -> list[dict[str, Any]]:
    p = effective(k0,p)
    return [
        {"year": year, "balance": future(k0,p,y)}
        for year in range(1, y+1)
    ]

def compare(plans: list[dict[str,Any]], y) -> tuple[str|None, float]:

    best_n: str | None = None
    best_balance: float = -1
    for plan in plans:
        p = effective(plan["k0"], plan["p"])
        balance = future(plan["k0"], p, y)
        if balance > best_balance:
            best_n, best_balance = plan["name"], balance
    return best_n, best_balance

plans: list[dict[str,Any]] = [
    {"name": "test1", "k0": 1000, "p": 0.03},
    {"name": "test2", "k0": 2000, "p": 0.01},
]
print(table(1000, 0.03, 5))
print(compare(plans,5))