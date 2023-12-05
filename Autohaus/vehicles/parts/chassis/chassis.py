import math

from ..base import Part

class Chassis(Part):
    def __init__(self, brand, size, age, milage, **kwargs) -> None:
        self.brand = brand
        self.size = size
        self.age = age
        self.milage = milage

    def calculate_condition(self):
        # exponential decay of chassis condition with age and milage
        # e^(-0.0005 * age) * e^(-0.0001 * milage)
        return math.exp(-0.0005 * self.age) * math.exp(-0.0001 * self.milage)