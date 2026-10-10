from decimal import Decimal, ROUND_HALF_UP

temp = 2.675
print(round(temp, 2))


print(Decimal(str(temp)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

