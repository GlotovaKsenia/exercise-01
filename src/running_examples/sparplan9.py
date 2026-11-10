p0 = 0.03
BONUS_AMOUNT = 5000
BONUS_P = 0.0005
class Acc:
    def __init__(self, balance):
        self.balance = balance

    def rate(self):
        raise NotImplementedError

    def deposit(self, amount):
        self.balance += amount

    def balance_future(self, y):
        return round(self.balance * (1 + self.rate()) ** y, 2)
    
class SavingAcc(Acc):
    p = p0
    def rate(self):
        if self.balance >= BONUS_AMOUNT:
            return round(self.p + BONUS_P, 4)
        return self.p

class FixedDeposit(Acc):
    def __init__(self, balance, fixed_rate):
        super().__init__(balance)
        self.fixed_rate = fixed_rate

    def rate(self):
        return self.fixed_rate

if __name__ == "__main__":
    accounts: list[Acc] = [
        SavingAcc(1000),
        SavingAcc(1000),
        FixedDeposit(1000, 0.025),
    ]

    for acc in accounts:
        print(type(acc).__name__, acc.balance_future(5))
        