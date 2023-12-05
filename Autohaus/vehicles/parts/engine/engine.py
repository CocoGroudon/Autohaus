from ..base import Part


class Engine(Part):
    def __init__(self, power, age, consumption, milage, **kwargs) -> None:
        self.power = power
        self.age = age
        self.consumption = consumption
        self.milage = milage