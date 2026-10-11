code = input("Artikelcode: ")
text = 0
no = 0
for i in code:
    if i.isalpha():
        text += 1
    elif i.isdigit():
        no += 1
    else:
        continue
print(f"Buchstaben: {text}")
print(f"Ziffern: {no}")