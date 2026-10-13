k0 = float(input("Startkapital:"))
p = int(input("Zinssatz: "))/100 + 1
years = 5
p_bonus = 0.005
k_bonus = 5000

add_year = 0

if p < 0:
    print("negativer Zinssatz")
else:
    if k0 >= k_bonus:
        p = round(p + p_bonus,4)

    k1 = round(k0 * p ** years,2)

    print(years, k1)

    if p == 0 or k0 <= 0:
        print("Kapital wächst nicht")
    else:
        target = k0 *2

    k2 = k1
    
    while k2 < target:
        add_year += 1
        k2 = k0 * p ** add_year

    print("Verdopplung nach", add_year, "Jahren")
        
