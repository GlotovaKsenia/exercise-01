import random
random.seed()
lena = jonas = round_no = 0

while lena <3 and jonas < 3:
    round_no +=1
    lena_r = random.randint(1,6)
    jonas_r = random.randint(1,6)
    print(f"Runde: {round_no}: Lena {lena_r}, Jonas {jonas_r}")

    if lena_r > jonas_r:
        lena +=1
    elif jonas_r > lena_r:
        jonas+=1
print(f"Lena: {lena}, Jonas {jonas}")