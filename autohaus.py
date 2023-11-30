import json
import os
import time
import shutil

from credentialManager import CredentialManager
import settings

class Car:
    def __init__(self, brand, model, price, **kwargs):
        self.cars_enum = -1 # -1 means not enumerated
        self.brand = brand
        self.model = model
        self.price = price
        if "image_path" in kwargs:
            self.image_path = kwargs["image_path"]
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
        if "owner" in kwargs:
            self.owner = kwargs["owner"]
        if "sold" in kwargs:
            self.sold = kwargs["sold"]
        
    def save_json(self, file):
        json.dump(self.__dict__, file)

    def load_json(self, json_string):
        data = json.loads(json_string)
        self.__dict__.update(data)
        return self


        

class Autohaus:
    def __init__(self):
        self.credentialManager = CredentialManager()
        self.user = None    


        # preload config in case it doesn't exist
        self.name = "Autohaus"
        self.cars = []
        self.cars_enum = 0
        self.known_models = {}

        self.load_config()
        self.load_cars()

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
        if not os.path.exists(os.path.join(settings.STATIC_DIR, "config.json")):
            self.save_config()
            return
        with open(os.path.join(settings.STATIC_DIR, "config.json"), "r") as f:
            data = json.load(f)
            if "cars_enum" in data:
                self.cars_enum = data["cars_enum"]
            if "known_models" in data:
                self.known_models = data["known_models"]
            if "name" in data:
                self.name = data["name"]

    def load_cars(self):
        for car in os.listdir(settings.CARS_DIR):
            with open(os.path.join(settings.CARS_DIR, car), "r") as f:
                data = json.load(f)
                self.cars.append(Car(**data))

    def save_dynamic_config(self):
        config_file = os.path.join(settings.STATIC_DIR, "config.json")

        with open(config_file, "r") as f:
            data = json.load(f)

        data["cars_enum"] = self.cars_enum

        with open(config_file, "w") as f:
            json.dump(data, f)


    def add_car(self, **kwargs):
        if "image_path" in kwargs:
            image_path = kwargs["image_path"]
            # copy image to settings.IMAGE_PATH/self.cars_enum-kwarg["brand"]-kwarg["model"]
            new_path = os.path.join(settings.CARS_DIR, f"{self.cars_enum} {kwargs['brand']}-{kwargs['model']}.png")
            shutil.copy(image_path, new_path)
            kwargs["image_path"] = new_path
            
        car = Car(**kwargs)

        car.cars_enum = self.cars_enum
        self.cars_enum += 1
        self.cars.append(car)

        carpath = os.path.join(settings.CARS_DIR, f"{car.cars_enum} {car.brand}-{car.model}.json")
        car.save_json(open(carpath, "w"))


    def get_cars(self):
        return self.cars

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