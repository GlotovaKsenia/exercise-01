import random
energy = 100
experience = 0
round = 1
#random.seed(7)
print("Start")

while True:
    if energy < 0 or round > 12:
        if energy < 0:
            print("zu wenig energy")
        else:
            print("gewonnen")
        break

    r = random.randint(5,20)
    energy -= r
    experience += 10
    print(f"Runde: {round} Energie: {energy}")
    round += 1

print(f"Ende. Erfahrung: {experience}")