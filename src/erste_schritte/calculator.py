no1 = float(input("Zahl1: "))
ao = input("Rechenzeichen (+, -, *, /): ")
no2 = float(input("Zahl2: "))

result = None

if ao == "+":
    result = no1 + no2

elif ao == "-":
    result = no1 - no2

elif ao == "*":
    result = no1 * no2

elif ao == "/" and no2 !=0 :
    result = no1 / no2

else: print("Fehler")

if result is not None:
    print(result)