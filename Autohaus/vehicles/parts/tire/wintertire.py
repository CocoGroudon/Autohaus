import math

from .tire import Tire


class WinterTire(Tire):
    def __init__(self, brand, size, age, milage, grip, spikes, **kwargs) -> None:
        super().__init__(brand, size, age, milage)
        self.grip = grip #friction coefficient between tire and road
        self.spikes = spikes # mechanical grip

        self.infotext = f"""
    Winterreifen:
        Marke:              {self.brand}
        Größe:              {self.size}
        Alter:              {self.age} Jahre
        Kilometerstand:     {self.milage} km
        Grip:               {self.grip}
        Grip im Schnee:     {self.spikes}
    """

    def get_required_values():
        return ["brand", "size", "age", "milage", "grip", "spikes"]

    def calculate_slip(self):
        # exponential decay of spikes, grip with age and milage
        # e^(-0.0005 * age) * e^(-0.0001 * milage) * e^(-0.0001 * spikes) * e^(-0.0001 * grip)
        return math.exp(-0.0005 * self.age) * math.exp(-0.0001 * self.milage) * math.exp(-0.0001 * self.spikes) * math.exp(-0.0001 * self.grip)