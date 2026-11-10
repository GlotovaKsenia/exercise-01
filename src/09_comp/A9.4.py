from typing import Protocol


class Receipt(Protocol):
    def render(self, total: float) -> str: ...

class TextReceipt:
    def render(self, total):
        return f"Summe: {total} Euro"
class ShortReceipt:
    def render(self, total):
        return f"{total} €"

def print_receipt(receipt: Receipt, total):
    return receipt.render(total)

print(print_receipt(TextReceipt(), 12.5))
print(print_receipt(ShortReceipt(), 12.5))
