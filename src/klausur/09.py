class Member:
    def __init__(self, name, fee):
        self.n = name
        self.f = fee

    def annual_fee(self):
        return self.f*12

class Vip(Member):
    def __init__(self, name, fee):
        super().__init__(name, fee)

    def annual_fee(self):
        return super().annual_fee() * 0.8

m1 = Member("Ali", 10)
v1 = Vip("Sam", 10)

print(m1.annual_fee()) #120
print(v1.annual_fee()) #96

