import math

from ..base import Part

class Tire(Part):
    def __init__(self, brand, size, age, milage, **kwargs) -> None:
        self.brand = brand
        self.size = size
        self.age = age
        self.milage = milage


    def calculate_condition(self):
        # exponential decay of tire condition with age and milage
        # e^(-0.0005 * age) * e^(-0.0001 * milage)
        return math.exp(-0.0005 * self.age) * math.exp(-0.0001 * self.milage)
    


    def get_required_values():
        return ["brand", "size", "age", "milage", "grip"]

    def calculate_grip(self):
        # exponential decay of grip with age and milage
        # e^(-0.0005 * age) * e^(-0.0001 * milage)
        return math.exp(-0.0005 * self.age) * math.exp(-0.0001 * self.milage)
    

    
