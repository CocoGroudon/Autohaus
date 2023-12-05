import math
        
from .chassis import Chassis
    
        
class LuxuryChassis(Chassis):
    def __init__(self, brand, size, age, milage, comfort, **kwargs) -> None:
        super().__init__(brand, size, age, milage)
        self.comfort = comfort # coolness factor of the chassis

        self.infotext = f"""
    Luxuschassis:
        Marke: {self.brand}
        Größe: {self.size}
        Alter: {self.age} Jahre
        Kilometerstand: {self.milage} km
        Komfort: {self.comfort}
    """

    def get_required_values():
        return ["brand", "size", "age", "milage", "comfort"]

    def calculate_comfort(self):
        # exponential decay of comfort with age and milage
        # e^(-0.0005 * age) * e^(-0.0001 * milage)
        return math.exp(-0.0005 * self.age) * math.exp(-0.0001 * self.milage)