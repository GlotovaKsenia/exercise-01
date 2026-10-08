import keyword

candidates = ["match", "price2", "net price", "GrossPrice", "None"]
for name in candidates:
    print(name, name.isidentifier(), keyword.iskeyword(name))

words = ["for", "match", "type", "gross_price", "None"]

for word in words:
    if keyword.iskeyword(word):
        type = "keyword"
    elif keyword.issoftkeyword(word):
        type = "softkeyword"
    else:
        type = "nothing of it"

    print(f"{word}: {type}")

def show_total(amount):
    print("Betrag:", amount)

show_total(19.99)

product = "brezel"
price = 0.9

print(f"{product} {price} Euro")