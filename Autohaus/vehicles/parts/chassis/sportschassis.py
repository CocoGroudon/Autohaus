import math

from .chassis import Chassis


class SportsChassis(Chassis):
    def __init__(self, brand, size, age, milage, airfriction, **kwargs) -> None:
        super().__init__(brand, size, age, milage)
        self.airfriction = airfriction 

        self.infotext = f"""
    Sportchassis:
        Marke: {self.brand}
        Größe: {self.size}
        Alter: {self.age} Jahre
        Kilometerstand: {self.milage} km
        Luftwiderstand: {self.airfriction}
    """

    def get_required_values():
        return ["brand", "size", "age", "milage", "airfriction"]

    def calculate_friction(self):
        # exponential decay of airfriction with age and milage
        # e^(-0.0005 * age) * e^(-0.0001 * milage)
        return math.exp(-0.0005 * self.age) * math.exp(-0.0001 * self.milage)
    
