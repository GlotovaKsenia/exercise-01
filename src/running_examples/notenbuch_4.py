note = float(input("Note: "))

if note <= 4.0:
    passed = True
    if note <= 1.5:
        stage = "sehr gut"
    elif note <= 2.5:
        stage = "gut"
    elif note <= 3.5:
        stage = "befriedigend"
    else:
        stage = "ausreichend"  # Das fängt jetzt exakt die 3.6 bis 4.0 ab
else:
    passed = False
    if note <= 5.0:  # (oder einfach else, da alles über 4.0 durchgefallen ist)
        stage = "mangelhaft"
    else:
        stage = "ungenügend"

print(f"Note {note}: {stage}, Bestanden: {passed}")