from pricing import gross_price

article = input("artikel: ")

net = float(input("Preis: "))
tex_rate = 19

print(gross_price(net, tex_rate))