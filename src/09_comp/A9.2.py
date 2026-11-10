from enum import Enum
class ProductGroup(Enum):
    BAKED_GOODS = "Backwaren"
    DRINKS = "Getränke"
    ACCESSORIES = "Zubehör"

print(ProductGroup.BAKED_GOODS.value)
print(len(ProductGroup))