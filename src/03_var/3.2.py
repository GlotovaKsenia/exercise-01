import math

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
x3 = int(input("x3: "))
y3 = int(input("y3: "))

side_a = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
side_b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
side_c = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
half_perimeter = (side_a + side_b + side_c) / 2

product = (half_perimeter * (half_perimeter - side_a) * (half_perimeter - side_b) * (half_perimeter - side_c))
area = math.sqrt(product)
print(f"Fläche: {area:.1f} FE")
