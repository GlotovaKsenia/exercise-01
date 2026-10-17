import math


def circle_area(r: float) -> float:
    area = math.pi * r **2
    return area

def circle_circumfence(r: float) -> float:
    circumfence = math.pi * 2 * r
    return circumfence

def total_area(r: list) -> float:
    overall = 0
    for i in r:
        overall += circle_area(i)
    return round(overall,2)

def total_circumfence(r: list) -> float:
    overall = 0
    for i in r:
        overall += circle_circumfence(i)
    return round(overall,2)

r = [5,8,3]
print(total_area(r))
print(total_circumfence(r))