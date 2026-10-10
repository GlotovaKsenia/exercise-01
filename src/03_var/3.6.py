name = "kaffee"
amount = 3
net_price = 1.68
taxes = 0.19

brut_price = round(net_price * (1 + taxes),2)
result = brut_price * amount

print(f"{name} {amount}x {brut_price:.2f} = {result:.2f}")