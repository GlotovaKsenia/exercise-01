amount = int(input("anzahl: "))
sale = 1
student = input("student?") == "ja"
if amount >= 10:
    sale = 0.95

brut = 0.5

result = brut * amount * sale
if student:
    result *= 0.9

print(f"{amount} Semmel: {result:.2f} Euro")