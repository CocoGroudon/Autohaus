import json
import os
import time
import shutil
from PIL import Image

from .credentialManager import CredentialManager
from .settings import Settings

class Vehicle:
    storage_path = None

    def __init__(self, brand, model, price, **kwargs):
        self.brand = brand
        self.model = model
        self.price = price

        self.vehicle_enum = None
        if "vehicle_enum" in kwargs:
            self.vehicle_enum = kwargs["vehicle_enum"]

        self.image = kwargs["image"] if "image" in kwargs else False
        self.fuel = None
        self.gearbox = None
        self.age = None
        self.color = None
        self.mileage = None
        self.power = None
        self.description = None
        self.sold = False

        if "fuel" in kwargs:
            self.fuel = kwargs["fuel"]
        if "gearbox" in kwargs:
            self.gearbox = kwargs["gearbox"]
        if "age" in kwargs:
            self.age = kwargs["age"]
        if "color" in kwargs:
            self.color = kwargs["color"]
        if "mileage" in kwargs:
            self.mileage = kwargs["mileage"]
        if "power" in kwargs:
            self.power = kwargs["power"]
        if "description" in kwargs:
            self.description = kwargs["description"]
        if "sold" in kwargs:
            self.sold = kwargs["sold"]
        
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

    def __init__(self, brand, model, price, **kwargs):
        super().__init__(brand, model, price, **kwargs)


class Motorcycle(Vehicle):
    # set path for motorcycles directory
    storage_path = Settings.MOTORCYCLES_DIR

    def __init__(self, brand, model, price, **kwargs):
        super().__init__(brand, model, price, **kwargs)






        

class Autohaus:
    def __init__(self):
        self.credentialManager = CredentialManager()
        self.user = None    

        self.known_types = {
            "Auto": Car,
            "Motorrad": Motorcycle
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
        print(brands)
        return brands
    
    def get_models(self, brand):
        try: # incase brand doesn't exist
            return self.known_models[brand]
        except KeyError:
            return []

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
        for type in self.known_types.keys():
            typeclass = self.known_types[type]
            directory = typeclass.storage_path
            for vehicle in os.listdir(directory):
                with open(os.path.join(directory, vehicle), "r") as f:
                    data = json.load(f)
                    self.vehicles.append(typeclass(**data))

    def save_dynamic_config(self):
        config_file = os.path.join(Settings.STATIC_DIR, "config.json")

        with open(config_file, "r") as f:
            data = json.load(f)

        data["vehicle_enum"] = self.vehicle_enum

        with open(config_file, "w") as f:
            json.dump(data, f)


    def add_vehicle(self, **kwargs):
        if "image_path" in kwargs.keys():
            if kwargs["image_path"]:
                image_path = kwargs["image_path"]
                new_path = os.path.join(Settings.IMAGE_DIR, f"{self.vehicle_enum}-{kwargs['brand']}-{kwargs['model']}.png")
                self.process_image(image_path, new_path)
                kwargs["image_path"] = new_path
            del kwargs["image_path"]
            kwargs["image"] = True
            
        vehicle = self.known_types[kwargs["vehicle_type"]](**kwargs)

        vehicle.vehicle_enum = self.vehicle_enum
        self.vehicle_enum += 1
        self.vehicles.append(vehicle)

        vehiclepath = os.path.join(vehicle.storage_path, f"{vehicle.vehicle_enum}-{vehicle.brand}-{vehicle.model}.json")
        vehicle.save_json(open(vehiclepath, "w"))

    def process_image(self, original_path, new_path):
        new_type = "PNG"
        new_size = (300, 300)
        image = Image.open(original_path)
        # Scale image so that it fitns into the new size but keeps the aspect ratio
        image.thumbnail(new_size, )
        # Save image
        image.save(new_path, new_type)


    def get_vehicles(self):
        return self.vehicles

    def get_fuels(self):
        return ["Benzin", "Diesel", "Elektro", "Hybrid"]

    def get_gearboxes(self):
        return ["Automatik", "Manuell"]

    
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