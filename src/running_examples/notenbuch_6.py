import sys
def mean(grades: list[float]) -> float:
    if not grades:  # Schutz vor Division durch Null bei leerer Liste
        return 0.0
    result = sum(grades) / len(grades)
    return round(result, 3)

def grade(grade: float) -> None:
    # Zuerst prüfen, ob die Note überhaupt im gültigen Bereich liegt
    if grade < 1.0 or grade > 6.0:
        print("ungültige note")
    elif grade <= 1.5:  # Schließt jetzt 1.0 bis 1.5 ein
        print("sehr gut")
    elif grade <= 2.5:
        print("gut")
    elif grade <= 3.5:
        print("befriedigend")
    elif grade <= 4.0:
        print("ausreichend")  # Tippfehler korrigiert
    else:
        print("nicht bestanden")

def passed(grade: float)-> bool:
    if grade < 1.0 or grade > 6.0:
            sys.exit()
    elif grade <= 4.0:
        return True
    else:
        return False

# Testlauf
grade(1.0)  # Ausgabe: sehr gut
grade(2.0)  # Ausgabe: gut
grade(0.5)  # Ausgabe: ungültige note

print(passed(3.0))
