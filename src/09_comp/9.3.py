class Vehicle:
    def __init__(self, brand, built_year):
        self.b = brand
        self.y = built_year

    def describe(self):
        return f"{self.b} ({self.y})"

class Car(Vehicle):
    def __init__(self, brand, built_year, horsepower):
        super().__init__(brand, built_year)
        self.p = horsepower
    def describe(self):
        return super().describe() + f", {self.p} PS"

class Bicycle(Vehicle):
    def __init__(self, brand, built_year, gears):
        super().__init__(brand, built_year)
        self.g = gears

    def describe(self):
        return super().describe()  + f", {self.g} Gänge"

class Fleet:
    def __init__(self, name, vehicle: list[Vehicle]= [], max_vehicles = 10):
        self.n = name
        self.v = vehicle
        self.max = max_vehicles

    def add(self, vehicle: Vehicle):
        self.v.append(vehicle)
        if len(self.v) > self.max:
            raise FleetFullError(self.max)

    def vehicle_count(self):
        return int(len(self.v))

    def car_count(self):
        car_count = 0
        for v in self.v:
            if isinstance(v, Car):
                car_count +=1
        return int(car_count)

class FleetFullError(Exception):
    def __init__(self, max_vehicles):
        self.max = max_vehicles
        super().__init__(f"Fuhrpark voll: maximal: {self.max} Fahrzeuge")


car = Car("kilomoto", 2022, 136)
bike = Bicycle("Radler", 2024, 21)
print(car.describe())
print(bike.describe())

fleet = Fleet("test",[],2)
fleet.add(car)
fleet.add(bike)

for v in fleet.v:
    print(v.describe())

print(fleet.vehicle_count(), fleet.car_count())
# car2 = Car("Tetst", 2000, 222)
# fleet.add(car2)