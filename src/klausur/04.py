open = input("Offen? (ja/nein)") == "ja"
staff = input("Personal? (ja/nein)") =="ja"

if open:
    if staff:
        print("geöffnet und personal")
    else:
        print("geöffnet und kein personal")
else:
    if staff:
        print("geschlossen, Personal da")
    else:
        print("geschlossen")