def receipt_line(name: str, quantity: int, amount:float)->str:
    return f"{name:<15}{quantity:>3} Stk {amount:>7.2f} €"
print(receipt_line("Brezel",2,4))