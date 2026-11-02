#Summe rekursiv
nr = [5,10,20]

def sum_list(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])

print(sum_list(nr))