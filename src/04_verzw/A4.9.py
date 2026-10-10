gewicht = 3
express = True
zuschlag = 0

if gewicht <= 1:
    if express:
        zuschlag = 4.0
    kosten = 3.9

elif gewicht <= 5:
    if express:
        zuschlag = 4.0
    kosten = 5.9

else:
    if express:
        zuschlag = 6.0
    kosten = 9.9

gesamt = kosten + zuschlag
print(gesamt)

