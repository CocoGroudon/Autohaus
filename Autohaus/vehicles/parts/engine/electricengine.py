import math

from .engine import Engine

class ElectricEngine(Engine):
    def __init__(self, power, age, consumption, milage, charge_cycles, **kwargs) -> None:
        super().__init__(power, age, consumption, milage)
        self.charge_cycles = charge_cycles

        self.infotext = f"""
    Elektromotor:
        Leistung: {self.power} kW
        Alter: {self.age} Jahre
        Verbrauch: {self.consumption} kWh/100km
        Kilometerstand: {self.milage} km
        Ladezyklen: {self.charge_cycles}
    """

    def get_required_values():
        return ["power", "age", "consumption", "milage", "charge_cycles"]

    def calculate_battery_condition(self):
        # exponential decay of battery capacity with charge cycles and age
        # 0.5 * e^(-0.0005 * charge_cycles) * e^(-0.01 * age)
        return 0.5 * math.exp(-0.0005 * self.charge_cycles) * math.exp(-0.01 * self.age)