def amount_days(year, month):
    # 1. Wenn der Monat ungerade ist (1, 3, 5, 7, 9, 11)
    if month % 2 != 0:
        days = 31
    # 2. Wenn der Monat gerade ist (2, 4, 6, 8, 10, 12)
    else:
        # 3. Wenn er NICHT 2 ist (also 4, 6, 8, 10, 12)
        if month != 2:
            days = 30
        # 4. Der konkrete Sonderfall für Februar (2)
        else:
            # Schaltjahr-Prüfung
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                days = 29
            else:
                days = 28
                
    return days

# Test:
print(amount_days(2024, 2))  # Gibt 29 aus (Schaltjahr)
print(amount_days(2023, 2))  # Gibt 28 aus (Kein Schaltjahr)
print(amount_days(2024, 4))  # Gibt 30 aus (gerader Monat != 2)
print(amount_days(2024, 3))  # Gibt 31 aus (ungerader Monat)