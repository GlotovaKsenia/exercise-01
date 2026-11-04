GRADES: dict[str, float] = {
    "Deniz": 1.3,
    "Lena": 1.7,
    "Jonas": 2.3,
    "Alex": 3.0,
    "Mika": 4.3,
    "Sam": 2.7
}

def ranking(grades: dict[str, float] = GRADES) -> list[tuple[str,float]]:
    return sorted(grades.items(), key=lambda item: item[1])

def grade_distribution(grades:dict[str,float]) -> dict[str, int]:
    distribution: dict[str, int] = {}
    for grade in grades.values():
        if grade <= 1.5:
            label = "sehr gut"
        elif grade <= 2.5:
            label = "gut"
        elif grade <= 3.5:
            label = "befriedigend"
        elif grade <= 4.0:
            label = "ausreichend"
        else:
            label = "nicht bestanden"
        distribution[label] = distribution.get(label, 0) + 1
    return distribution

print(ranking(GRADES))
print(grade_distribution(GRADES))