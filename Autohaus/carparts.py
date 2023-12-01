import math

class Part:
    def get_data(self):
        data = self.__dict__.copy()
        data["type"] = self.__class__.__name__
        return data
    


class Motor(Part):
    def __init__(self, power, age, consumption, milage) -> None:
        self.power = power
        self.age = age
        self.consumption = consumption
        self.milage = milage

class CombustionEngine(Motor):
    def __init__(self, power, age, consumption, milage, fuel_type) -> None:
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

class ElectricEngine(Motor):
    def __init__(self, power, age, consumption, milage, charge_cycles) -> None:
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



class Gearbox(Part):
    def __init__(self) -> None:
        pass

class ManualGearbox(Gearbox):
    def __init__(self, gears) -> None:
        super().__init__()
        self.gears = gears
        self.displayname = f"Manuell {gears} Gänge"

        self.infotext = f"""
    Manuelles Getriebe:
        Gänge: {self.gears}
    """

    def get_required_values():
        return ["gears"]

class AutomaticGearbox(Gearbox):
    def __init__(self) -> None:
        super().__init__()
        self.displayname = "Automatik"

        self.infotext = f"""
    Automatik Getriebe
    """

    def get_required_values():
        return  []




class Tire(Part):
    def __init__(self, brand, size, age, milage) -> None:
        self.brand = brand
        self.size = size
        self.age = age
        self.milage = milage


    def calculate_condition(self):
        # exponential decay of tire condition with age and milage
        # e^(-0.0005 * age) * e^(-0.0001 * milage)
        return math.exp(-0.0005 * self.age) * math.exp(-0.0001 * self.milage)
    
class SportsTire(Tire):
    def __init__(self, brand, size, age, milage, grip) -> None:
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

    def get_required_values():
        return ["brand", "size", "age", "milage", "grip"]

    def calculate_grip(self):
        # exponential decay of grip with age and milage
        # e^(-0.0005 * age) * e^(-0.0001 * milage)
        return math.exp(-0.0005 * self.age) * math.exp(-0.0001 * self.milage)
    
class WinterTire(Tire):
    def __init__(self, brand, size, age, milage, grip, spikes) -> None:
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
    
class SummerTire(Tire):
    def __init__(self, brand, size, age, milage, drip) -> None:
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




class Chassis(Part):
    def __init__(self, brand, size, age, milage) -> None:
        self.brand = brand
        self.size = size
        self.age = age
        self.milage = milage

    def calculate_condition(self):
        # exponential decay of chassis condition with age and milage
        # e^(-0.0005 * age) * e^(-0.0001 * milage)
        return math.exp(-0.0005 * self.age) * math.exp(-0.0001 * self.milage)
    
class SportsChassis(Chassis):
    def __init__(self, brand, size, age, milage, airfriction) -> None:
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
    
class LuxuryChassis(Chassis):
    def __init__(self, brand, size, age, milage, comfort) -> None:
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