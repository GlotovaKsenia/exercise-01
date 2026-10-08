# first_test_demo.py
# Add-in Kapitel 2: eine Funktion, die ihr mit eurer ersten Testdatei prüft.
def gross_price(net_price):
    return round(net_price * 1.19, 2)

print(gross_price(0.47))


def test_gross_price(gross_price):
    assert gross_price() == 0.56

if test_gross_price:
    print("passt")
else:
    print("ne")