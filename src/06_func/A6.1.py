# addin_checkout_typed.py
TAX_FOOD = 0.07
TAX_STANDARD = 0.19
QUANTITY_DISCOUNT_THRESHOLD = 10
QUANTITY_DISCOUNT_RATE = 0.05


def gross_price(net: float, tax_rate: float) -> float:
    """Bruttopreis: Nettopreis plus Steuer, auf Cent gerundet.

    >>> gross_price(0.84, TAX_FOOD)
    0.9
    >>> gross_price(1.68, TAX_STANDARD)
    2.0
    """
    return round(net * (1 + tax_rate), 2)


def apply_discount(amount: float, rate: float) -> float:
    """Betrag nach Abzug eines Rabattsatzes, auf Cent gerundet.

    >>> apply_discount(16.26, 0.10)
    14.63
    """
    return round(amount * (1 - rate), 2)


def line_total(price: float, quantity: int) -> float:
    """Positionsbetrag: Bruttopreis mal Menge, ab 10 Stück mit Mengenrabatt.

    >>> line_total(0.90, 9)
    8.1
    >>> line_total(0.90, 10)
    8.55
    >>> line_total(0.90, 13)
    11.11
    """
    # Positionsbetrag vor dem Rabatt runden (Geschäftsregel „Reihenfolge“,
    # case-study/README.md): 0.9 * 13 ergibt als float 11.700000000000001,
    # spätes Runden ergäbe 11.12 statt der vorgegebenen 11.11.
    total = round(price * quantity, 2)
    if quantity >= QUANTITY_DISCOUNT_THRESHOLD:
        total = apply_discount(total, QUANTITY_DISCOUNT_RATE)
    return total


def receipt_line(name: str, quantity: int, amount: float) -> str:
    """Eine ausgerichtete Bonzeile: Artikel, Menge und Betrag.

    >>> receipt_line("Kaffee", 3, 6.0)
    'Kaffee           3 Stk     6.00 €'
    """
    return f"{name:<15}{quantity:>3} Stk  {amount:>7.2f} €"


if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    print(f"doctest: {result.attempted - result.failed}/{result.attempted} Beispiele bestanden")


# Folien: slides/session-06-functions-and-modules.md, Termin 6
# Übung: exercises/exercise-06.md, Aufgabe V6.1
# Lösung: exercises/solutions/solution-06.md, Aufgabe V6.1
