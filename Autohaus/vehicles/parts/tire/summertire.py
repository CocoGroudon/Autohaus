import math

from .tire import Tire


class SummerTire(Tire):
    def __init__(self, brand, size, age, milage, drip, **kwargs) -> None:
        super().__init__(brand, size, age, milage)
        self.drip = drip # coolness factor of the tire

        self.infotext = f"""
    Sommerreifen:
        Marke: {self.brand}
        Größe: {self.size}
        Alter: {self.age} Jahre
        Kilometerstand: {self.milage} km
        Grip: {self.drip}
    """

    def get_required_values():
        return ["brand", "size", "age", "milage", "drip"]

    def calculate_drip(self):
        # exponential decay of drip with age and milage
        # e^(-0.0005 * age) * e^(-0.0001 * milage)
        return math.exp(-0.0005 * self.age) * math.exp(-0.0001 * self.milage)