from abc import ABC, abstractmethod

class ShippingMethod(ABC):
    @abstractmethod
    def cost(weight_kg):
        pass

class StandardShipping(ShippingMethod):
    def __init__(self, weight_kg):
        self.w = weight_kg
    def cost(self):
        return round(2.5 + self.w*0.5,2)

class ExpressShipping(ShippingMethod):
    def __init__(self, weight_kg):
        self.w = weight_kg
    def cost(self):
        return round(6 + 0.8*self.w,2)

for shipping_method in [StandardShipping(2), ExpressShipping(2)]:
    print(type(shipping_method).__name__, shipping_method.cost())