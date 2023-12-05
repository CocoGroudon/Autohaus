import math

from .engine import Engine

class CombustionEngine(Engine):
    def __init__(self, power, age, consumption, milage, fuel_type, **kwargs) -> None:
        super().__init__(power, age, consumption, milage)
        self.fuel_type = fuel_type

        self.infotext = f"""
    Verbrennungsmotor:
        Leistung: {self.power} kW
        Alter: {self.age} Jahre
        Verbrauch: {self.consumption} l/100km
        Kilometerstand: {self.milage} km
        Kraftstoff: {self.fuel_type}
"""

    def get_required_values():
        return ["power", "age", "consumption", "milage", "fuel_type"]

    def calculate_emissions(self):
        # bases on consumption and fuel
        # e^(-0.0005 * consumption) * e^(-0.0001 * fuel)
        return math.exp(-0.0005 * self.consumption) * math.exp(-0.0001 * self.fuel_type)
    
    def calculate_efficiency(self):
        # bases on consumption milage age and power
        # e^(-0.0005 * milage) * e^(-0.01 * age) * e^(-0.0001 * power) * e^(-0.0005 * consumption)
        return math.exp(-0.0005 * self.milage) * math.exp(-0.01 * self.age) * math.exp(-0.0001 * self.power) * math.exp(-0.0005 * self.consumption)