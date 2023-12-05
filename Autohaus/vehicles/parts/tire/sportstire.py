from .tire import Tire  

class SportsTire(Tire):
    def __init__(self, brand, size, age, milage, grip, **kwargs) -> None:
        super().__init__(brand, size, age, milage)
        self.grip = grip # friction coefficient between tire and road

        self.infotext = f"""
    Sportreifen:
        Marke: {self.brand}
        Größe: {self.size}
        Alter: {self.age} Jahre
        Kilometerstand: {self.milage} km
        Grip: {self.grip}
    """