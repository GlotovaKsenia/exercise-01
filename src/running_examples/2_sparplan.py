kapital = float(input("Startkapital: ").replace(",","."))
percentage = int(input("Zinssatz in Prozent: "))/100
years = int(input("Vergangene Jahre: "))
for i in range(1, years + 1):
    kapital = kapital * (percentage + 1)
print("Kapital nach", years, "Jahr ist:", kapital)