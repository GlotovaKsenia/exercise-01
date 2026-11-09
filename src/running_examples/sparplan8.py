from dataclasses import dataclass
@dataclass
class SavingPlan:
    k0: float
    p: float

    def balance(self, y):
        return round(self.k0 * (1 + self.p)**y, 2)

    def deposit(self, amount):
        self.balance += amount

print(SavingPlan(1000, 0.03).balance(5))