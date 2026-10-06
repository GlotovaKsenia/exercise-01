name = input("Name Studentin: ")
grade = round(float(input("Note: ").replace(",",".")), 1)

print(f"{name} hat die Note: {grade}")
print(name, "hat die Note", grade + ".")