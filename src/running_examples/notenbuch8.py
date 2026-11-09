class Student:
    def __init__(self, name, grade:float):
        self.n = name
        self.g = grade

class Course:
    def __init__(self, name, students: list[Student] | Student | None = None):
        self.n = name
        self.students = students if students is not None else []
        self.students = []
        if students is not None:
            self.add_student(students)

    def add_student(self, student_input: Student | list[Student]):
        if isinstance(student_input, list):
            self.students.extend(student_input)
        else:
            self.students.append(student_input)

    def average(self):
        if not self.students:
            return 0.0
        total = sum(s.g for s in self.students)
        return round(total / len(self.students), 2)

    def best_student(self):
        if not self.students:
            return None
        best = min(self.students, key=lambda student: student.g )


# ==========================================
# TESTDATEN ERSTELLEN & KURSE BEFÜLLEN
# ==========================================

# Kurs 1: Komplett leer starten
kurs_leer = Course("Philosophie")

# Kurs 2: Direkt mit einer vorgefertigten Liste von Studenten starten
mathe_studenten = [
    Student("Lena", 1.3),
    Student("Jonas", 3.7),
    Student("Alex", 2.3)
]
kurs_mathe = Course("Höhere Mathematik", mathe_studenten)

# Kurs 3: Mit einem einzelnen Studenten starten und später eine Liste nachladen
kurs_info = Course("Einführung in Python", Student("Mia", 2.0))

# Weitere Studenten für den Info-Kurs vorbereiten
weitere_studenten = [
    Student("Tim", 1.0),
    Student("Sofia", 3.0)
]
# Ganze Liste auf einmal hinzufügen
kurs_info.add_student(weitere_studenten)


# ==========================================
# TEST-AUSGABEN (PRINT-LOOP)
# ==========================================

alle_kurse = [kurs_leer, kurs_mathe, kurs_info]

print("=== START DER KURS-ANALYSE ===\n")

for kurs in alle_kurse:
    print(f"Kurs: {kurs.n}")
    print(f"  Anzahl Studierende: {len(kurs.students)}")
    print(f"  Notendurchschnitt:  {kurs.average()}")
    
    bester = kurs.best_student()
    if bester:
        name, note = bester
        print(f"  Beste/r im Kurs:    {name} (Note: {note})")
    else:
        print("  Beste/r im Kurs:    Keine Studierenden im Kurs")
        
    print("-" * 35)

print("\n=== TEST BEENDET ===")