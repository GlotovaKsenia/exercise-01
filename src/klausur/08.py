class Employee:
    def __init__(self, name, salary):
        self.n = name
        self.s = salary

    def introduce(self):
        return self.n, self.s

    def salary_raise(self, percentage):
        self.s = round(self.s * (1 + percentage),2)
        #return round(self.salary, 2)

e1 = Employee("Noah", 3000)
e1.salary_raise(0.05)

e2 = Employee("Yuki", 3200)
print(e1.introduce())
print(e2.introduce())

class Ingredient:
    def __init__(self, name, amount):
        self.n = name
        self.a = amount
    def __str__(self):
        return f"{self.n} {self.a}"
    def __repr__(self):
        return f"Ingredient({self.n!r}, {self.a!r})"

lentils = Ingredient("Linsen", 250)
print("------------------------")
print(lentils)
print(repr(lentils))
print([lentils])
print("----------------------------")

class Recipe:
    def __init__(self, name):
        self.n = name
        self.i: list[Ingredient] = []

    def add_ingredient(self, ingredient: Ingredient):
        if ingredient.a <= 0:
            raise ValueError("Menge darf nicht 0 oder kleiner sein")
        self.i.append(ingredient)

    def show(self):
            total = 0
            print("Rezept:", self.n),
            for i in self.i:
                print(i.n, i.a)
                total += i.a
            print("Gesamt", total)

r = Recipe("Linsensuppe")

l = Ingredient("Linsen", 250)
k = Ingredient("Karotten", 150)
b = Ingredient("Bruhe", 500)

r.add_ingredient(l)
r.add_ingredient(k)
r.add_ingredient(b)

r.show()

employee:[Employee] = [e1, e2]

def total_payroll(employee):
    total = 0
    for e in employee:
        total += e.s
    print(round(total, 2))

def highest_pay(employee):
    highest = max(employee, key=lambda emp: emp.s)
    return highest

total_payroll(employee)
print(highest_pay(employee).n)

