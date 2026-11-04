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

monday: list[str] = ["Lena","Jonas","Lena","Mika"]
tuesday: list[str] = ["Jonas","Alex","Mika"]

m = set(monday)
t = set(tuesday)
print(len(m))
print(sorted(m & t))
print(sorted(m | t))

morning: list[str] = ["Brezel","Kaffee"]
evening = morning
backup = morning[:]
evening.append("Semmel")
backup.append("Wasser")
print(morning) # brezel kaffee semmel
print(evening) #brezel kaffee semmel
print(backup) #brezel kaffee wasser