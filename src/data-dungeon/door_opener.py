messwerte = [12,15,11,14,48]
average = sum(messwerte)/len(messwerte)

def door(wert, alarm_status):
  if alarm_status is None:
    print(f"{wert} Grenzwert")
  elif alarm_status:
    print(f"{wert} Gefahr, Tür wird geöffnet")
  else:
    print(f"{wert} unauffällig")

for wert in messwerte:
  if wert == average * 2:
    alarm = None
  elif wert > average * 2:
    alarm = True
  else:
    alarm = False
  door(wert, alarm)
