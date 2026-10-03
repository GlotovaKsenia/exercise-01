net_price = [0.84, 0.47, 1.68, 1.01, 2.52]
summe = 0
for i in range (1, 6):
    summe = summe + net_price[i-1]
print(end="Gesamt Summe:\n",)
print(summe)
print("Gesamtsumme: ", round(sum(net_price), 2))