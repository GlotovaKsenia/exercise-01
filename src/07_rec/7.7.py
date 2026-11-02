orders: dict[str, int] = {}
def for_orders(name, anzahl):
    if name in orders:
        orders[name] += anzahl
    else:
        orders[name] = anzahl
while True:
    name = input("Name: ").strip()
    if not name:
        break

    try:
        anzahl = int((input("Anzahl: ")))
    except ValueError:
        print("keine anzahl")
    else:
        if anzahl <=0:
            print("ungültige Zahl")
            continue
    print(f"Anzahl: {anzahl} angenommen")
    for_orders(name, anzahl)

    print(orders)

