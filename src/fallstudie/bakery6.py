import checkout

STUDENT_DISCOUNT_RATE = 0.10


def read_order() -> float:
    order_total = 0.0
    while True:
        name = input("Artikel: ").strip()
        if name == "":
            break
        net_price = float(input("Nettopreis in Euro: "))
        quantity = int(input("Menge: "))

        if quantity <= 0:
            print("Menge muss positiv sein, Position wird übersprungen.")
            continue

        gross = checkout.gross(net_price, 0.19)
        amount = checkout.line_total(gross, quantity)
        print(checkout.receipt_line(name, quantity, amount))
        order_total += amount

    return order_total


def main() -> None:
    print("Bäckerei Berger: Kassensystem")
    customer_type = input("Kundentyp (studierend/normal): ").strip().lower()
    print("Bon beginnt, leere Artikeleingabe beendet den Bon.")

    order_total = read_order()
    if customer_type == "studierend":
        order_total = checkout.discount(order_total, STUDENT_DISCOUNT_RATE)

    print(f"Summe: {order_total:.2f} €")


if __name__ == "__main__":
    main()