TAX_FOOD = 0.07
TAX_STANDART = 0.19

#Teil 2:
PRICE_PER_KG = 4.80
weight_1 = 510
weight_2 = 480

price_1 = weight_1 * PRICE_PER_KG/1000
price_2 = weight_2 * PRICE_PER_KG/1000

print(f"{price_1:.2f}, {price_2:.2f}")

price = 2.755
from decimal import Decimal, ROUND_HALF_UP

result = Decimal(str(price)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(result)