def power(base, exponent: int):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(power(2,5))

DEVICES = {
    101: "beamer",
    102: "pc",
    103: "microphone"
}

def get_device(number: int):
    return DEVICES.get(number, "ungültig")

try:
    i = int(input("number: "))
except ValueError:
    print("keine Zahl")
else:
    print(get_device(i))