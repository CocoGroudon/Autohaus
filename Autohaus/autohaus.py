import json
import os

from .credentialManager import CredentialManager
from .settings import Settings
from . import vehicles



known_vehicle_types = vehicles.known_types

known_parts_types = {}

known_parts_types.update(known_vehicle_types)
known_parts_types.update(vehicles.parts.known_types)
print(f"known parts types: {known_parts_types}")



        

class Autohaus:
    Settings = Settings
    def __init__(self):
        self.credentialManager = CredentialManager()
        self.user = None    

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
        for type in known_vehicle_types.keys():
            typeclass = known_vehicle_types[type]
            directory = typeclass.storage_path
            for vehicle in os.listdir(directory):
                with open(os.path.join(directory, vehicle), "r") as f:
                    data = json.load(f)
                    self.vehicles.append(self.build_part(data))
    
    def build_part(self, data):
        data = data.copy()

        parts = data["parts"] if "parts" in data else []
        for part_key in parts: # infinite part inception possible
            part = parts[part_key]
            data[part_key] = self.build_part(part)

        type = data["type"]
        typeclass = known_parts_types[type]
        del data["type"]
        part = typeclass(**data)
        print(f"finished building {type}", part)
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

        with open(vehiclepath, "w") as f:
            json.dump(vehicle_data, f)

        self.save_dynamic_config()



    
    def set_user(self, user):
        self.user = user

    def close(self):
        self.save_dynamic_config()
        self.logout()

    def logout(self):
        self.user = None

if __name__ == "__main__":
    autohaus = Autohaus()
