def future_value(k0: float, p: float, y: int)-> float:
    result = k0 * (p+1)**y
    return round(result,2)

def years_target(k0: float, p: float, k1: float)-> int:
    years = 0
    while k0 < k1:
        k0 = k0 * (p+1)
        years +=1
    return years

print(years_target(1000,0.03,2000))