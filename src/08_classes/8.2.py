from math import pi

class Circle:
    def __init__(self, radius):
        self.r = radius

    def area(self):
        return round(pi*self.r**2, 2)

    def circumference(self):
        return round(2*pi*self.r, 2)

    def sticker_price(self, price_per_cm2: float = 0.05):
        total = Circle.area(self) * price_per_cm2
        return round(total, 2)
    @classmethod
    def from_diameter(cls, diameter):
        return cls(radius=diameter/2)

test = Circle.from_diameter(4)
print(test.r)
print(test.area())

class Rectangle:
    def __init__(self, width, length):
        self.w = width
        self.l = length

    def area(self):
        return round(self.w * self.l, 2)

    def perimeter(self):
        return 2*(self.w + self.l)

    def storage_cost(self, price_per_m2: float = 12.5):
        total = Rectangle.area(self) * price_per_m2
        return round(total, 2)

class StorageUnit:
    units_built = 0
    def __init__(self, name, length, width, height):
        self.n = name
        self.l = length
        self.w = width
        self.h = height
        StorageUnit.units_built += 1
    @classmethod
    def built_so_far(cls):
        return cls.units_built

    @staticmethod
    def volume_from_dimensions(width, height, length):
        return width*height*length


    def volume(self):
        return round(self.l * self.h * self.w, 2)

    def price(self, pp_m3 = 50):
        total = StorageUnit.volume(self) * pp_m3
        return round(total, 2)

print("-----------------------")
print(StorageUnit.built_so_far())
print(StorageUnit.volume_from_dimensions(2,2,2))
print("-----------------------")
class Car:
    def __init__(self, brand, model, year, mileage = 0):
        self.b = brand
        self.m = model
        self.y = year
        self._mileage = mileage
    @classmethod
    def from_text(cls, line):
        brand, model, year, mileage = line.split(";")
        return cls(brand, model, year, mileage)

    def drive(self, km):
        if km<=0:
            raise ValueError("KM need to be positiv")
        self._mileage += km


    def __str__(self):
        return f"{self.b} {self.m} ({self.y}), {self._mileage} km"

print(Car.from_text("Test;modell;2000;"))

class Article:
    vat_rate = 0.07

    def __init__(self, name, net_price):
        self.n = name
        self.np = net_price

    def gross_price(self):
        return round(self.np * (1+self.vat_rate),2)

pretzel = Article("Brezel",0.84)
coffee = Article("Kaffee", 1.68)
coffee.vat_rate = 0.19
print(pretzel.gross_price(), coffee.gross_price())

Article.vat_rate = 0.1
print(pretzel.gross_price(), coffee.gross_price())
print("------------------------")

circle = Circle(4)
rectangle = Rectangle(2, 1.5)

print(circle.area(), circle.circumference(), circle.sticker_price())

print(rectangle.area(), rectangle.perimeter(), rectangle.storage_cost())

s1 = StorageUnit("Spind klein", 1, 0.5, 2)
s2 = StorageUnit("Spind groß", 2, 1, 2)

print(s1.volume(), s2.price(), StorageUnit.units_built)

fleet: list[Car] = [
    Car("Toyota", "Corollo", 2018, 1000),
    Car("Honda", "Civic", 2020, 5000)
]

for car in fleet:
    car.drive(150)
    print(car)