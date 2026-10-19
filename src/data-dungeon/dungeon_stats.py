import random
def mean(values: list[float])->float:
    x = sum(values)/len(values)
    return round(x,2)

def median(values: list[float])->float:
    sorted_values = sorted(values)
    x = len(sorted_values)//2
    return sorted_values[x]


def is_outlier(value: float, values: list[float]) -> bool:
    for i in values:
        if i >= value*2:
            return True
    return False 

def roll_dice(low: int, high: int)-> int:
    return random.randint(low,high)