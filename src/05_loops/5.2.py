lines = ["Bäckerei Berger","Brezel 0.90 Eur","Kaffee 2.00 Eur"]
length = 0
for line in lines:
    if len(line)>length:
        length = len(line)
    else:
        pass

print("*"*(length+4))
for i in lines:
    print("* "+i+" *")
print("*"*(length+4))