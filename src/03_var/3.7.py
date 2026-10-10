date = "2026-09-27"
no = 4231

year = date[0:4]
month = date[5:7]
day = date[8:]

date = day+"."+month+"."+year
print(f"Beleg Nr. 0{no} vom {date}")
