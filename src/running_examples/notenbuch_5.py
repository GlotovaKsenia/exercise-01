import sys
grades = []
note = input("Note eingeben: ")
while note != "":
    answer = float(note)
    if not (answer >= 1.0 and answer <= 6.0):
        print("ungültig")
        sys.exit()
    grades.append(float(answer))
    note = input("Note eingeben: ")
if len(grades) == 0:
    print("keine Noten in der Liste")
print(grades)
average = sum(grades)/len(grades)
best = min(grades)
lowest = max(grades)
print("Durchschnitt:", round(average,2))
print("Beste Note:", best)
print("Schlechteste Note:", lowest)

passed = []

for i in grades:
    if i <= 4.0:
        passed.append(i)

bestanden = len(passed)

print("Bestanden:", bestanden, "von", len(grades))