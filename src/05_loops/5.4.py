quantities = [3,-1,5,0,2]
valid_sum = 0
skipped = 0

for quantity in quantities:
    if quantity <= 0:
        skipped += 1
        continue
    valid_sum += quantity

print("Summe gültiger Mengen:", valid_sum)
print("Übersprungen:", skipped)