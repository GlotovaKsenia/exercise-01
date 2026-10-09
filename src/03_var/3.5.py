# betrag = int(input("Rückgeld in Cent: "))

# euro_2 = betrag//200
# rest = betrag%200
# print("2 Euro: ", euro_2, rest)

# euro_1 = rest//100
# rest = rest%100
# print("1 Euro: ", euro_1, rest)

# cent_50 = rest//50
# rest = rest%50
# print("50 cent: ", cent_50, rest)

# cent_20 = rest//20
# rest = rest%20
# print("20 cent: ", cent_20, rest)

# cent_10 = rest//10
# rest = rest%10
# print("10 cent: ", cent_10, rest)

wechselgeld = [100,50,20,10,5,2,1,0.5,0.2,0.1]

rest = float(input("Restgeld: "))

for geld in wechselgeld:
    anzahl = rest//geld
    rest = rest%geld
    print(geld,": ", anzahl)