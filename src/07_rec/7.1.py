daily_revenue: list[float] = [412.50, 380.0, 512.75, 290.0, 601.20]

low_revenue: list[float] = [amount for amount in daily_revenue if amount < 400]
rounded: list[int] = [round(amount * 100) for amount in daily_revenue]

print(low_revenue)
print(rounded)

drinks = ["Kaffee","Wasser"]
drinks.append("Tee")
drinks.insert(1,"Saft")
p=drinks.pop()
print(drinks, p)

mengen=[3,12,8,15,1,10]
rabatt = [anzahl for anzahl in mengen if anzahl >=10]
print(rabatt)
pers = ["p1","p2","p3","p4","p5","p6"]

for i in range (0,5):
    print(pers[i],mengen[i])

bestell: dict[str, int] = dict(zip(pers, mengen))
print(bestell)
bestell["p7"] = 17

def gesamt(liste: list[int])-> int:
    if not liste:
        return 0
    return liste[0] + gesamt(liste[1:])
# 3 + gesamt([12, 8, 15, 1, 10])
# 3 + 12 + gesamt([8, 15, 1, 10])
# ...
# 3 + 12 + 8 + 15 + 1 + 10 + gesamt([])

print(gesamt(mengen))