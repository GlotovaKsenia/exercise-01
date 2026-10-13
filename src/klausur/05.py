no = 5
while no > 0:
    print(no)
    no -= 1

print("Start!")

prices = [2,5]
for i in range(1,4): #4 Durchläufe
    for price in prices:#2 Durchläufe
        print(i, "stück zu", price, "Euro: ", i * price)
# 1 stück zu 2 Euro: 2
# 1 Stück zu 5 Euro: 5
# 2
# 3
# 4 Stück zu 2 Euro: 8
# 4 Stück zu 5 Euro: 20

prices = [2,5]
for i in range(1,4): #3 Durchläufe
    print(i, "Stück:", end=" ")
    for price in prices:#2 Durchläufe
        print(i*price, end=" ")
    print(end="\n")

pos = ["brezel","semmel","kaffee"]
for i in range(1, len(pos)+1): #len(pos)= 3 schleife läuft: 1 dann 2 dann ende also nur 2 mal, außerdem ist der erste platz index 0
    print(i, pos[i-1])

stock = 8
sold = 0
while stock > 5: #stock ist konstant, muss bei 1 verkauft um 1 sinken
    sold += 1
    stock -= 1
print("verkauft: ", sold)