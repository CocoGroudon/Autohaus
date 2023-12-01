import json
import os
import time
import shutil
from PIL import Image
import math

from .credentialManager import CredentialManager
from .settings import Settings
from .carparts import *


import pickle
def save_car(objekt):
    with open("D:\Schule\Info\Autohaus\Autohaus\car.pkl", 'wb') as datei:
        pickle.dump(objekt, datei)






class Vehicle:
    storage_path = None

    def __init__(self, brand, model, price, color, description, image_path, **kwargs):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.image_path = image_path

        self.description = description
        self.sold = False

        self.vehicle_enum = None
        if "vehicle_enum" in kwargs:
            self.vehicle_enum = kwargs["vehicle_enum"]

        
    def save_json(self, file):
        json.dump(self.__dict__, file)

    def load_json(self, json_string):
        data = json.loads(json_string)
        self.__dict__.update(data)
        return self
    
    def get_image(self):
        if not self.image:
            return None
        path = os.path.join(Settings.IMAGE_DIR, f"{self.vehicle_enum}-{self.brand}-{self.model}.png")
        return path

class Car(Vehicle):
    # set path for cars directory
    storage_path = Settings.CARS_DIR

    def __init__(self, brand, model, price, color, description, image_path, engine:Motor, gearbox:Gearbox, tire:Tire, chassis:Chassis,  **kwargs):
        super().__init__(brand, model, price, color, description, image_path)
        print(engine)
        print(gearbox)
        print(tire)
        print(chassis)
        self.parts = {
            "engine": engine,
            "gearbox": gearbox,
            "tire": tire,
            "chassis": chassis
        }

    def get_data(self):
        data = self.__dict__.copy()
        data["type"] = self.__name__
        partsdict  = {}
        for parttype in self.parts.keys():
            part = self.parts[parttype]
            partsdict[parttype] = part.get_data()
        data["parts"] = partsdict
        return data

    def build_from_data(self, data): #TODO: test
        self.__dict__.update(data)
        for parttype in self.parts.keys():
            part = self.parts[parttype]
            partdata = data["parts"][parttype]
            part.__dict__.update(partdata)




class Motorcycle(Vehicle):
    # set path for motorcycles directory
    storage_path = Settings.MOTORCYCLES_DIR

    def __init__(self, brand, model, price, **kwargs):
        super().__init__(brand, model, price, **kwargs)





        

class Autohaus:
    Settings = Settings
    def __init__(self):
        self.credentialManager = CredentialManager()
        self.user = None    


        self.known_vehicle_types = {
            "Car": Car,
            "Motorcycle": Motorcycle
        }

        self.known_parts_types = {
            "Motor": Motor,
            "CombustionEngine": CombustionEngine,
            "ElectricEngine": ElectricEngine,

            "Gearbox": Gearbox,
            "ManualGearbox": ManualGearbox,
            "AutomaticGearbox": AutomaticGearbox,

            "Tire": Tire,
            "WinterTire": WinterTire,
            "SummerTire": SummerTire,
            "SportsTire": SportsTire,

            "Chassis": Chassis,
            "SportsChassis": SportsChassis,
            "LuxuryChassis": LuxuryChassis

        }

        # preload config in case it doesn't exist
        self.name = "Autohaus"
        self.vehicles = []
        self.vehicle_enum = 0
        self.known_models = {}

        self.load_config()
        self.load_vehicles()

    def get_brands(self):
        brands = self.known_models.keys()
        return brands
    
    def get_models(self, brand):
        try: # incase brand doesn't exist
            return self.known_models[brand]
        except KeyError:
            return []
        
    def get_vehicles(self):
        return self.vehicles
        
    def get_engines(self):
        return {
            "Verbrenner": CombustionEngine,
            "Elektro": ElectricEngine
        }

    def get_fuels(self):
        return ["Benzin", "Diesel", "Elektro", "Hybrid"]

    def get_gearboxes(self):
        return {
            "Automatik": AutomaticGearbox,
            "Manuell": ManualGearbox
        }
    
    def get_tires(self):
        return {
            "Winter": WinterTire,
            "Sommer": SummerTire,
            "Sport": SportsTire
        }
    
    def get_chassis(self):
        return {
            "Sport": SportsChassis,
            "Luxus": LuxuryChassis
        }

    def load_config(self):
        # test if config exists
        if not os.path.exists(os.path.join(Settings.STATIC_DIR, "config.json")):
            self.save_config()
            return
        with open(os.path.join(Settings.STATIC_DIR, "config.json"), "r") as f:
            data = json.load(f)
            if "vehicle_enum" in data:
                self.vehicle_enum = data["vehicle_enum"]
            if "known_models" in data:
                self.known_models = data["known_models"]
            if "name" in data:
                self.name = data["name"]

    def load_vehicles(self):
        for type in self.known_vehicle_types.keys():
            typeclass = self.known_vehicle_types[type]
            directory = typeclass.storage_path
            for vehicle in os.listdir(directory):
                with open(os.path.join(directory, vehicle), "r") as f:
                    data = json.load(f)
                    self.vehicles.append(self.build_vehicle(data))

    def build_vehicle(self, data):
        type = data["type"]
        typeclass = self.known_vehicle_types[type]
        parts = data["parts"]
        for part_key in parts:
            part = parts[part_key]
            parts[part_key] = self.build_part(part)

        vehicle = typeclass(engine=parts["engine"], gearbox=parts["gearbox"], tire=parts["tire"], chassis=parts["chassis"], **data)
        # print(f"finished building {vehicle.brand} {vehicle.model}")
        return vehicle
    
    def build_part(self, data):
        type = data["type"]
        del data["type"]
        typeclass = self.known_parts_types[type]
        part = typeclass(**data)
        # print(f"finished building {type}", part)
        return part


    def save_dynamic_config(self):
        config_file = os.path.join(Settings.STATIC_DIR, "config.json")

        with open(config_file, "r") as f:
            data = json.load(f)

        data["vehicle_enum"] = self.vehicle_enum

        with open(config_file, "w") as f:
            json.dump(data, f)


    def add_vehicle(self, vehicle):
        vehicle.vehicle_enum = self.vehicle_enum
        self.vehicle_enum += 1

        self.vehicles.append(vehicle)
        vehiclepath = os.path.join(vehicle.storage_path, f"{vehicle.vehicle_enum}-{vehicle.brand}-{vehicle.model}.json")
        vehicle_data = vehicle.get_data()

        save_car(vehicle)



    
    def set_user(self, user):
        self.user = user

    def close(self):
        self.save_dynamic_config()
        self.logout()

    def logout(self):
        self.user = None

if __name__ == "__main__":
    autohaus = Autohaus()
    # autohaus.process_image("D:\Schule\Info\\2015-GL-Class-GL450.png", "D:\Schule\Info\Autohaus\Autohaus\static\images\\0-Mercedes-AMG.png")